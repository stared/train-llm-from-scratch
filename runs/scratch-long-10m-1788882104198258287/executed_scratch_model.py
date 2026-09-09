"""Small causal decoder, initialized entirely from random weights."""
from dataclasses import dataclass, asdict
import math
import torch
from torch import nn
from torch.nn import functional as F


@dataclass
class Config:
    vocab_size: int = 8192
    width: int = 320
    layers: int = 6
    heads: int = 5
    hidden: int = 896
    context: int = 256


def config_for(size, vocab_size=8192):
    if size == '10m':
        return Config(vocab_size=vocab_size)
    if size == '30m':
        return Config(vocab_size=vocab_size,width=512,layers=8,heads=8,hidden=1408)
    if size == '100m':
        return Config(vocab_size=vocab_size,width=768,layers=12,heads=12,hidden=2304)
    raise ValueError('Choose10m,30m or100m')


class Attention(nn.Module):
    def __init__(self, c):
        super().__init__()
        self.heads, self.dim = c.heads, c.width // c.heads
        if self.dim % 2 or c.width % c.heads:
            raise ValueError('Even head dimension required')
        self.qkv = nn.Linear(c.width,3*c.width,bias=False)
        self.proj = nn.Linear(c.width,c.width,bias=False)
        frequencies = 1. / (10000 ** (torch.arange(0,self.dim,2).float()/self.dim))
        angles = torch.outer(torch.arange(c.context).float(),frequencies)
        self.register_buffer('cos',angles.cos(),persistent=False)
        self.register_buffer('sin',angles.sin(),persistent=False)

    def rotate(self,x):
        cos=self.cos[:x.shape[-2]].to(x.dtype)[None,None]
        sin=self.sin[:x.shape[-2]].to(x.dtype)[None,None]
        a,b=x[...,0::2],x[...,1::2]
        return torch.stack((a*cos-b*sin,a*sin+b*cos),dim=-1).flatten(-2)

    def forward(self,x):
        batch, length, width=x.shape
        q,k,v=self.qkv(x).view(batch,length,3,self.heads,self.dim).permute(2,0,3,1,4).unbind(0)
        y=F.scaled_dot_product_attention(self.rotate(q),self.rotate(k),v,is_causal=True,dropout_p=0.)
        return self.proj(y.transpose(1,2).contiguous().view(batch,length,width))


class Block(nn.Module):
    def __init__(self,c):
        super().__init__()
        self.norm1=nn.RMSNorm(c.width)
        self.attention=Attention(c)
        self.norm2=nn.RMSNorm(c.width)
        self.gate=nn.Linear(c.width,c.hidden,bias=False)
        self.up=nn.Linear(c.width,c.hidden,bias=False)
        self.down=nn.Linear(c.hidden,c.width,bias=False)

    def forward(self,x):
        x=x+self.attention(self.norm1(x))
        z=self.norm2(x)
        return x+self.down(F.silu(self.gate(z))*self.up(z))


class ScratchGPT(nn.Module):
    def __init__(self,c):
        super().__init__()
        self.config=c
        self.embedding=nn.Embedding(c.vocab_size,c.width)
        self.blocks=nn.ModuleList([Block(c) for _ in range(c.layers)])
        self.norm=nn.RMSNorm(c.width)
        self.apply(self.initialize)
        for name,p in self.named_parameters():
            if name.endswith(('attention.proj.weight','down.weight')):
                nn.init.normal_(p,mean=0.,std=.02/math.sqrt(2*c.layers))

    @staticmethod
    def initialize(module):
        if isinstance(module,(nn.Linear,nn.Embedding)):
            nn.init.normal_(module.weight,mean=0.,std=.02)

    def forward(self,ids,targets=None):
        if ids.shape[1]>self.config.context:
            raise ValueError('Context exceeded')
        x=self.embedding(ids)
        for block in self.blocks:
            x=block(x)
        x=self.norm(x)
        if targets is None:
            return F.linear(x[:,-1,:],self.embedding.weight).float()
        logits=F.linear(x,self.embedding.weight)
        return F.cross_entropy(logits.reshape(-1,logits.shape[-1]).float(),targets.reshape(-1))

    @torch.no_grad()
    def generate(self,ids,new_tokens=128,temperature=.8,top_k=50):
        self.eval()
        for _ in range(new_tokens):
            logits=self(ids[:,-self.config.context:])/temperature
            threshold=logits.topk(min(top_k,logits.shape[-1]),dim=-1).values[:,-1,None]
            logits=logits.masked_fill(logits<threshold,-float('inf'))
            ids=torch.cat([ids,torch.multinomial(logits.softmax(-1),1)],dim=1)
        return ids
