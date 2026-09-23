"""Standard tokenizer comparisons, using their reference implementation."""
def tokenize(request):
    import tiktoken
    name, text = request.get('tokenizer'), request.get('text')
    if name not in ('cl100k_base', 'o200k_base'):
        raise ValueError('Unknown tokenizer.')
    if not isinstance(text, str) or len(text) > 2000:
        raise ValueError('Use up to 2,000 characters.')
    encoding = tiktoken.get_encoding(name)
    ids = encoding.encode(text, disallowed_special=())
    tokens = []
    for token_id in ids:
        raw = encoding.decode_single_token_bytes(token_id)
        try:
            label = raw.decode('utf-8').replace(' ', '·').replace('\n', '↵').replace('\t', '⇥')
        except UnicodeDecodeError:
            label = raw.hex(' ').upper()
        tokens.append(dict(id=token_id, label=label, hex=raw.hex(' ')))
    return dict(text=text, ids=ids, initial=[tokens], steps=[], standard=True)
