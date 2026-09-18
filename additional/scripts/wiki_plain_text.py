"""Importable CPU worker for the optional plain-Wikipedia comparison."""
import mwparserfromhell
from prepare_wiki_scratch import strip_reference_tags


def clean_wiki_text(original):
    text=strip_reference_tags(original)
    text=str(mwparserfromhell.parse(text).strip_code(normalize=True,collapse=True))
    return ' '.join(text.split())
