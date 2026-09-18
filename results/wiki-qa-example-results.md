# Wikipedia model: before and after question-answer SFT

**Model:** ScratchGPT-300M (291M parameters), trained from random weights on Polish Wikipedia markup, then supervised fine-tuning (SFT) on 8,912 short definitions. Each fact has eight question forms and 30 training presentations.

Pretraining on B200: **83.3 min / $9.13**. SFT on H100: **13.6 min / $1.01**. Worker estimates; audit inference, controller and storage are separate.

## Fresh wording audit

The same 200 questions before and after SFT. Ten fresh question forms and different facts from the earlier probes; all answers belong to the SFT training dataset. Neither half of this audit selected or tuned a checkpoint.

| Pretraining | Before SFT | After SFT |
|---|---:|---:|
| Raw Wikipedia / 133min (earlier run) | 0/200 | 190/200 |
| Raw Wikipedia / 83min B200 | 0/200 | 190/200 |
| Wikipedia prose / 83min B200 | 0/200 | 197/200 |

![Fresh definition-question audit](wiki-qa-fresh-audit.svg)

## Actual answers from the 83-minute markup model

Fourth audit test item and first exact-match failure. Baseline excerpts end after four lines or 120 characters; trained outputs are unchanged.

| Question | Before SFT | After SFT |
|---|---|---|
| Pomóż mi zrozumieć hasło „Zegar”. | <br>„Zegar”<br><br>„Zegar”<br>… [truncated] | Przyrząd do ciągłego pomiaru i wskazywania czasu. |
| Dokończ krótką definicję hasła „Cement”:  | <br>:: ''Cement''<br>:: ''Cement''<br>:: ''Cement''<br>… [truncated] | Historyczna mieszanina dwóch lub więcej związków chemicznych lub pierwiastków chemicznych. |

- [Zegar](https://pl.wikipedia.org/w/index.php?oldid=80508488): reference answer — Przyrząd do ciągłego pomiaru i wskazywania czasu.
- [Cement](https://pl.wikipedia.org/w/index.php?oldid=78323560): reference answer — Hydrauliczne spoiwo mineralne.

This measures answering supplied definitions under new wording. The gain combines learning the question-answer format and rehearsing the facts; it does not establish general instruction following or unseen knowledge. Exact matching can reject valid paraphrases.

Recorded checkpoints: `night-1789689694697165000-300m-B200-5000s` → `night-1789696207346333000-291m-raw-best-varied` (`sft-final.pt`). Audit SHA256: `35d3e0b901b3f212fb7cac8660c1ba542b8394f2ac2738b285801cad0031a3d6`.
