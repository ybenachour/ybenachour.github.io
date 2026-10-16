import json, html, re
from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT

ROOT=Path(__file__).parent
data=json.loads((ROOT/'content.json').read_text())
pubs=[p for p in data['publications'] if p['status']!='Submitted']
esc=html.escape
rows=[]
for p in pubs:
    link=f'<a href="https://doi.org/{esc(p["doi"])}" target="_blank" rel="noopener noreferrer">Read paper <span aria-hidden="true">↗</span></a>' if p['doi'] else '<span class="awaiting">Accepted manuscript</span>'
    rows.append(f'''<article class="publication" data-type="{p['type']}" data-status="{p['status']}"><div class="pub-year">{p['year']}<span>{p['type']}</span></div><div><div class="pub-status">{p['status']}</div><h3>{esc(p['title'])}</h3><p class="authors">{esc(p['authors'])}</p><p class="venue">{esc(p['venue'])}</p>{link}</div></article>''')
template=(ROOT/'template.html').read_text()
(ROOT/'index.html').write_text(template.replace('<!-- PUBLICATIONS -->','\n'.join(rows)).replace('PUBLICATION_COUNT',str(len(pubs))),encoding='utf-8')

# Public edition: omit personal identifiers, reference contacts and dated metrics.
text=data['cv']
text=re.sub(r'BIBLIOMETRIC SUMMARY\n.*?(?=EDUCATION)', '', text, flags=re.S)
before, after=text.split('\nPUBLICATIONS\n',1)
after=after.split('\nEDITORIAL AND PEER-REVIEW SERVICE\n',1)[1]
text=before+'\nEDITORIAL AND PEER-REVIEW SERVICE\n'+after
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyCV',fontName='Helvetica',fontSize=9.2,leading=13,spaceAfter=5,textColor=colors.HexColor('#253345')))
styles.add(ParagraphStyle(name='HeadCV',fontName='Helvetica-Bold',fontSize=10.5,leading=14,spaceBefore=15,spaceAfter=7,textColor=colors.HexColor('#143647'),keepWithNext=True))
styles.add(ParagraphStyle(name='NameCV',fontName='Helvetica-Bold',fontSize=25,leading=30,spaceAfter=8,textColor=colors.HexColor('#143647')))
story=[Paragraph('Dr. Yassine Benachour',styles['NameCV']),Paragraph('PhD · FHEA · PMP | Academic curriculum vitae',styles['BodyCV']),Paragraph('Higher Colleges of Technology · Dubai, UAE<br/>ybenachour@yahoo.fr · orcid.org/0000-0003-3141-0830',styles['BodyCV']),Spacer(1,9)]
for line in text.splitlines():
    line=line.strip()
    if not line: continue
    line=line.replace('—','-').replace('–','-').replace('‑','-').replace('→','to').replace('×','x')
    heading=line.isupper() and len(line)<90
    line=re.sub(r'^1\.\s*','• ',line)
    story.append(Paragraph(esc(line),styles['HeadCV'] if heading else styles['BodyCV']))
story.append(Paragraph('PUBLICATIONS AND ACCEPTED CONFERENCE PAPERS',styles['HeadCV']))
for i,p in enumerate(pubs,1):
    citation=f"{i}. {p['authors']}. {p['title']}. {p['venue']}, {p['year']}. {p['status']}."
    if p['doi']: citation+=' DOI: '+p['doi']
    story.append(Paragraph(esc(citation),styles['BodyCV']))
def footer(c,d):
    c.setStrokeColor(colors.HexColor('#d6ddd9'));c.line(44,39,551,39)
    c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#596b70'))
    c.drawString(44,26,'Yassine Benachour | Public academic CV | Prepared October 2026')
    c.drawRightString(551,26,str(d.page))
SimpleDocTemplate(str(ROOT/'Yassine_Benachour_CV.pdf'),pagesize=(595.28,841.89),rightMargin=44,leftMargin=44,topMargin=43,bottomMargin=53,title='Yassine Benachour - Academic CV',author='Yassine Benachour').build(story,onFirstPage=footer,onLaterPages=footer)
print(f'Built index.html and public CV, {len(pubs)} publication records.')
