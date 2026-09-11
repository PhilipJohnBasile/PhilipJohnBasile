"""Transparent, theme-aware artwork for the continuous profile fieldbook.

Requires fonttools. Interaction belongs to native README details and links;
SVG animation is a finite introduction, never a simulated pointer control.
"""
from pathlib import Path
from html import escape
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.roundingPen import RoundingPen

A = Path(__file__).resolve().parents[1] / 'assets'
FONT = TTFont(A / 'anton-regular.ttf')
GS, CM = FONT.getGlyphSet(), FONT.getBestCmap()
UNIT = FONT['head'].unitsPerEm
RED = '#d94a3e'

def display(text, x, y, size, color):
    result, cursor = [], 0
    for char in text:
        glyph = GS[CM[ord(char)]]
        pen = SVGPathPen(GS)
        glyph.draw(RoundingPen(pen, roundFunc=lambda n: round(n, 2)))
        result.append(f'<path transform="translate({cursor} 0)" d="{pen.getCommands()}"/>')
        cursor += glyph.width
    return f'<g fill="{color}" transform="translate({x} {y}) scale({size/UNIT} {-size/UNIT})">'+''.join(result)+'</g>'

def text(value, x, y, size, color, family='monospace', italic=False):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}"'+(' font-style="italic"' if italic else '')+f'>{escape(value)}</text>'

def path(d, color=RED, width=2, extra=''):
    length = ' pathLength="1700"' if 'thread' in extra else ''
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{length} {extra}/>'

def plus(x, y, color):
    return f'<circle cx="{x}" cy="{y}" r="20" fill="none" stroke="{color}"/>'+path(f'M{x-7} {y}h14m-7 -7v14',color,2)

def write(slug, w, h, body, title, theme, mobile=False, motion=False):
    css = '''<style>
    @keyframes arrive{from{opacity:.15;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
    @keyframes trace{from{stroke-dashoffset:1700}to{stroke-dashoffset:0}}
    .a{animation:arrive .8s ease-out both}.b{animation:arrive 1.15s ease-out both}.c{animation:arrive 1.5s ease-out both}
    .thread{stroke-dasharray:1700;animation:trace 3.8s cubic-bezier(.2,.7,.3,1) both}
    @media(prefers-reduced-motion:reduce){.a,.b,.c,.thread{animation:none!important}}
    </style>''' if motion else ''
    name=f'field-{slug}'+('-mobile' if mobile else '')+f'-{theme}.svg'
    (A/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>{css}{body}</svg>\n')

for theme, ink, muted in [('light','#252a30','#59636e'),('dark','#eeeae2','#a6aaa9')]:
    for mobile in [False, True]:
        w,h=(600,650) if mobile else (1200,590)
        b=text('PHILIP JOHN BASILE',12,31,19,ink)
        b+=text('ENGINEER / MAKER / SINCE 1998',12,58,13,muted)
        if mobile:
            for word,y,size,c,cls in [('MAKE',218,143,ink,'a'),('SOMETHING',361,133,ink,'b'),('MATTER.',506,143,RED,'c')]:
                b+=f'<g class="{cls}">'+display(word,6,y,size,c)+'</g>'
            b+=path('M12 529C154 513 270 531 405 518',RED,3,'class="thread"')
            b+=text('From the first web page',12,573,27,ink,'Georgia,serif',True)
            b+=text('to the next token.',12,606,27,ink,'Georgia,serif',True)
            b+=text('CLICK TO UNFOLD THE CONNECTIONS',12,644,16,muted)+plus(566,624,RED)
        else:
            for word,y,c,cls in [('MAKE',215,ink,'a'),('SOMETHING',359,ink,'b'),('MATTER.',503,RED,'c')]:
                b+=f'<g class="{cls}">'+display(word,5,y,146,c)+'</g>'
            b+=text('From the first',806,156,38,ink,'Georgia,serif',True)
            b+=text('web page',806,203,38,ink,'Georgia,serif',True)
            b+=text('to the next',806,250,38,ink,'Georgia,serif',True)
            b+=text('token.',806,297,38,ink,'Georgia,serif',True)
            b+=path('M1122 125C1210 145 1148 385 982 363S802 399 854 445S1158 513 1167 542C1168 570 492 534 10 532',RED,2,'class="thread"')
            b+=text('CREATIVE SYSTEMS → LOCAL AI',806,470,15,muted)
            b+=text('CLICK TO UNFOLD THE CONNECTIONS',12,582,17,muted)+plus(1161,568,RED)
        write('hero',w,h,b,'Make something matter. Click or press Enter to unfold the connections behind my work.',theme,mobile,True)

        # The connecting thread, revealed by the native hero disclosure.
        sw,sh=(600,310) if mobile else (1200,180)
        b=path('M20 18C80 100 85 280 560 282' if mobile else 'M20 30C172 168 1000 163 1170 30',RED,2,'class="thread"')
        labels=[('DATA','Source & prepare'),('MODELS','Train & measure'),('RUNTIMES','Make it run'),('AGENTS','Give it tools'),('PEOPLE','Make it useful')]
        for i,(name,sub) in enumerate(labels):
            x=30 if mobile else 18+i*242
            y=28+i*56 if mobile else 40
            b+=text(f'0{i+1}',x,y,13,RED)+display(name,x+34,y+5,26,ink)
            b+=text(sub,255 if mobile else x+34,y+1 if mobile else y+33,17,muted)
        write('connections',sw,sh,b,'Data to models to runtimes to agents to people. The whole system is the work.',theme,mobile,True)

        # Open, borderless headings. The page itself supplies the background.
        for slug,num,title,eyebrow in [
            ('upstream','01','Good code travels.','CONTRIBUTING UPSTREAM'),
            ('models','02','The model is a beginning.','HUGGING FACE / MODELS, DATA & DEMOS'),
            ('work','03','Make the whole thing work.','RUNTIMES / AGENTS / PRODUCTION'),
            ('about','04','A long way from hello world.','THE PERSON / THE WORK / THE THROUGH-LINE'),
            ('writing','05','Leave a paper trail.','NOTES / EXPERIMENTS / OPEN QUESTIONS')]:
            hw,hh=(600,130) if mobile else (1200,158)
            b=text(num,12,35,15,RED)+text(eyebrow,54,35,13 if mobile else 16,muted)
            b+=text(title,10,94 if mobile else 112,36 if mobile else 66,ink,'Georgia,serif')
            b+=path(f'M12 {hh-12}q30 -6 68 -2',RED,2)
            write(slug,hw,hh,b,title+' '+eyebrow.capitalize(),theme,mobile)

        for slug,number,title,sub in [('wisp','01','WISP CODER','TOKENIZER → TRAINING → RELEASE'),('agents','02','AGENT SYSTEMS','BUSINESS TOOLS, HUMAN JUDGMENT'),('local','03','LOCAL INFERENCE','WEIGHTS, MEMORY, METAL, STORAGE'),('rag','04','RAG & RELEASES','RETRIEVAL THAT EARNS ITS PLACE')]:
            cw,ch=(600,120) if mobile else (1200,122)
            b=text(number,8,51,17,RED)+display(title,55,66,44 if mobile else 62,ink)
            b+=text(sub,57,100,14 if mobile else 18,muted)+plus(cw-30,55,RED)
            write('case-'+slug,cw,ch,b,f'Open or close {title.title()}. {sub.capitalize()}.',theme,mobile)

        cw,ch=(600,170) if mobile else (1200,170)
        b=text('SOMETHING WORTH BUILDING?',12,30,15,muted)
        b+=text('Let’s make a useful dent.',9,97,43 if mobile else 70,ink,'Georgia,serif',True)
        b+=text('START A CONVERSATION ↗',12,146,17,RED)
        write('contact',cw,ch,b,'Let’s make a useful dent. Start a conversation.',theme,mobile)

print('Built transparent desktop/mobile artwork for light and dark themes.')
