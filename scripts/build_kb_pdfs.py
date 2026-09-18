from pathlib import Path
import re, shutil
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/"gemini"/"gem"/"source"
OUT=ROOT/"gemini"/"gem"
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
pdfmetrics.registerFont(TTFont("DV",FONT))
pdfmetrics.registerFont(TTFont("DVB",BOLD))
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name="T",parent=styles["Title"],fontName="DVB",fontSize=18,leading=22,alignment=TA_CENTER,spaceAfter=14))
styles.add(ParagraphStyle(name="H1",parent=styles["Heading1"],fontName="DVB",fontSize=13,leading=17,spaceBefore=10,spaceAfter=6))
styles.add(ParagraphStyle(name="H2",parent=styles["Heading2"],fontName="DVB",fontSize=10.5,leading=14,spaceBefore=7,spaceAfter=4))
styles.add(ParagraphStyle(name="B",parent=styles["BodyText"],fontName="DV",fontSize=8.8,leading=12.3,spaceAfter=5))
styles.add(ParagraphStyle(name="S",parent=styles["BodyText"],fontName="DV",fontSize=7.8,leading=10.5,spaceAfter=3))
styles.add(ParagraphStyle(name="CODE",parent=styles["BodyText"],fontName="DV",fontSize=8,leading=10.8,leftIndent=8,rightIndent=8,spaceAfter=5,backColor=colors.whitesmoke))
def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def inline(s):
    s=esc(s)
    s=re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>",s)
    return s
def make(src):
    lines=src.read_text(encoding="utf-8").splitlines()
    title=lines[0].lstrip("# ").strip()
    story=[Paragraph(inline(title),styles["T"])]
    i=1
    while i<len(lines):
        line=lines[i].strip()
        if not line:
            i+=1; continue
        if line.startswith("## "):
            story.append(Paragraph(inline(line[3:]),styles["H1"])); i+=1; continue
        if line.startswith("### "):
            story.append(Paragraph(inline(line[4:]),styles["H2"])); i+=1; continue
        if line.startswith("|") and i+1<len(lines) and lines[i+1].strip().startswith("|---"):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith("|"):
                parts=[p.strip() for p in lines[i].strip().strip("|").split("|")]
                if not all(set(p)<=set("-: ") for p in parts):
                    rows.append(parts)
                i+=1
            data=[[Paragraph(inline(c),styles["S"]) for c in row] for row in rows]
            if data:
                t=Table(data,repeatRows=1,hAlign="LEFT")
                t.setStyle(TableStyle([("FONTNAME",(0,0),(-1,0),"DVB"),("GRID",(0,0),(-1,-1),0.3,colors.lightgrey),("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4),("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
                story += [t,Spacer(1,6)]
            continue
        if line.startswith("- "):
            story.append(Paragraph("• "+inline(line[2:]),styles["B"])); i+=1; continue
        if "→" in line or line.startswith("NATURALNESS >") or line.startswith("DETAIL PICK"):
            story.append(Paragraph(inline(line),styles["CODE"])); i+=1; continue
        story.append(Paragraph(inline(line),styles["B"])); i+=1
    target=OUT/(src.stem+".pdf")
    SimpleDocTemplate(str(target),pagesize=A4,rightMargin=40,leftMargin=40,topMargin=40,bottomMargin=40,title=title).build(story)
    return target
for old in OUT.glob("*.pdf"):
    old.unlink()
for p in sorted(SRC.glob("*.md")):
    make(p)
print("Built",len(list(OUT.glob("*.pdf"))),"PDFs")
