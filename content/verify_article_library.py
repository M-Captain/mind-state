"""Compare actual rendered paragraph text with independent OOXML source reads."""
import hashlib
import json
import os
import sys
import xml.etree.ElementTree as ET
import zipfile
from html.parser import HTMLParser
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
os.environ.setdefault('DJANGO_SETTINGS_MODULE','web.settings')
import django
django.setup()
from django.test import Client, override_settings
from alpha.models import LandingContent

class SourceParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.paragraphs=[]
        self.current=None
        self.depth=0
        self.placements=[]
        self.images=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'data-source-paragraph' in attrs:
            assert self.current is None
            self.current=[int(attrs['data-source-paragraph']), '']
            self.depth=1
        elif self.current is not None and tag not in ['img','br','input','link','meta']:
            self.depth+=1
        if 'data-after-source-paragraph' in attrs:
            self.placements.append((int(attrs['data-after-source-paragraph']),self.paragraphs[-1][0]))
        if tag=='img' and attrs.get('src','').startswith('/static/articles/'):
            self.images.append(attrs['src'])
    def handle_endtag(self,tag):
        if self.current is not None:
            self.depth-=1
            if self.depth==0:
                self.paragraphs.append(tuple(self.current))
                self.current=None
    def handle_data(self,text):
        if self.current is not None:
            self.current[1]+=text

def original_text(paragraph):
    texts=[]
    for n in paragraph.iter():
        tag=n.tag.rsplit('}',1)[-1]
        if tag=='t': texts.append(n.text or '')
        elif tag in ['br','cr']: texts.append('\n')
        elif tag=='tab': texts.append('\t')
        elif tag=='noBreakHyphen': texts.append('\u2011')
        elif tag=='softHyphen': texts.append('\u00ad')
    return ''.join(texts)

catalog=json.loads((ROOT/'content/article-library.json').read_text(encoding='utf-8'))
client=Client()
with override_settings(ALLOWED_HOSTS=['testserver']):
    for item in catalog:
        source=ROOT/'content/source_articles'/item['source_document']
        assert hashlib.sha256(source.read_bytes()).hexdigest()==item['source_sha256']
        with zipfile.ZipFile(source) as doc:
            body=ET.fromstring(doc.read('word/document.xml')).find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}body')
            paras=body.findall('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')
        first,last=item['source_paragraph_range']
        expected=[(i+1,original_text(p)) for i,p in enumerate(paras) if first<=i+1<=last]
        response=client.get(f"/app/article/{item['id']}/")
        assert response.status_code==200
        page=response.content.decode('utf-8')
        parsed=SourceParser(); parsed.feed(page)
        assert parsed.paragraphs==expected, item['title']
        assert len(parsed.placements)==2 and all(anchor==preceding for anchor,preceding in parsed.placements)
        assert [x[0] for x in parsed.placements]==[x['after_source_paragraph'] for x in item['image_placements']]
        assert all(image['src'] in page for image in item['images'])
        own_folder=item['images'][0]['src'].rsplit('/',1)[0]+'/'
        assert len([url for url in parsed.images if url.startswith(own_folder)])==4
        assert '7 October 2026' in page
        obj=LandingContent.objects.get(pk=item['id'])
        assert obj.title==item['title'] and obj.author==item['author']
        assert str(obj.published_at)==item['publication_date']
        print('PASS', item['title'], len(expected), 'unchanged paragraphs; exact image anchors')
    assert LandingContent.objects.filter(section=LandingContent.ARTICLES).count()==11
    for url in ['/','/app/search/']:
        response=client.get(url)
        assert response.status_code==200
        page=response.content.decode('utf-8')
        for item in catalog:
            assert f"/app/article/{item['id']}/" in page
        assert 'Sturgill Simpson' not in page and 'Wade Warren' not in page
    assert client.get('/app/article/1/').status_code==404
    page=client.get('/app/search/',{'q':'Sanja'}).content.decode('utf-8')
    assert '/app/article/1007/' in page and '/app/article/1001/' not in page
print('PASS all 11 rendered articles, 748 exact paragraphs, 55 images, listing coverage, author search, and removal of demo URLs.')
