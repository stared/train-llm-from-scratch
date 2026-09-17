import bz2
import tempfile
from pathlib import Path
import unittest
from prepare_wiki_scratch import iter_articles,article_split,strip_reference_tags


class WikitextExtractionTests(unittest.TestCase):
    def test_plain_variant_preserves_prose_between_different_references(self):
        text='Warszawa<ref name="populacja" /> jest stolicą Polski.<ref>Źródło\nz przypisem.</ref> Leży nad Wisłą.'
        self.assertEqual(strip_reference_tags(text),'Warszawa jest stolicą Polski. Leży nad Wisłą.')
        self.assertEqual(strip_reference_tags('A<ref/>B<ref name="x"/>C'),'ABC')

    def test_preserves_markup_decodes_xml_and_filters_namespace(self):
        xml='''<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.11/">
        <page><title>Test</title><ns>0</ns><id>1</id><revision><id>8</id><model>wikitext</model><text xml:space="preserve">''' + "'''Test''' [[Polska|PL]] {{Infobox|x=1}}\n== Historia ==\n&lt;ref&gt;A &amp; B&lt;/ref&gt;\n{|\n| tabelka\n|}" + '''</text></revision></page>
        <page><title>Template:X</title><ns>10</ns><id>2</id><revision><text>Skip me</text></revision></page>
        <page><title>Alias</title><ns>0</ns><id>3</id><redirect title="Test"/><revision><text>#PATRZ [[Test]]</text></revision></page>
        </mediawiki>'''
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'dump.xml.bz2';p.write_bytes(bz2.compress(xml.encode()))
            rows=list(iter_articles(p))
        self.assertEqual([r['id'] for r in rows],['1','3'])
        self.assertEqual(rows[0]['text'],"'''Test''' [[Polska|PL]] {{Infobox|x=1}}\n== Historia ==\n<ref>A & B</ref>\n{|\n| tabelka\n|}")
        self.assertTrue(rows[1]['redirect'])
        self.assertEqual(rows[1]['text'],'#PATRZ [[Test]]')
        self.assertEqual(article_split(rows[0]['text']),article_split(rows[0]['text']))


if __name__=='__main__':unittest.main()
