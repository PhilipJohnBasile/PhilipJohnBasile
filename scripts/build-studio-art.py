"""Build the interactive-profile edition using self-contained vector artwork.

Motion finishes within five seconds and respects prefers-reduced-motion. Actual
interaction lives in README links and native details/summary controls.
Requires fonttools. No external graphics service or runtime dependencies.
"""
from pathlib import Path
from html import escape
from math import cos, sin, pi
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.roundingPen import RoundingPen

A = Path(__file__).resolve().parents[1] / 'assets'
FONT = TTFont(A / 'anton-regular.ttf')
GS, CM = FONT.getGlyphSet(), FONT.getBestCmap()
UNIT = FONT['head'].unitsPerEm
INK, PAPER, RED, MUTED = '#191918', '#e8e5dd', '#d93b2c', '#aaa395'

def display(text, x, y, size, color=PAPER):
    items, cursor = [], 0
    for char in text:
        name = CM[ord(char)]
        pen = SVGPathPen(GS)
        GS[name].draw(RoundingPen(pen, roundFunc=lambda n: round(n, 2)))
        items.append(f'<path transform="translate({cursor} 0)" d="{pen.getCommands()}"/>')
        cursor += GS[name].width
    return f'<g fill="{color}" transform="translate({x} {y}) scale({size/UNIT} {-size/UNIT})">'+''.join(items)+'</g>'

def mono(text, x, y, size=16, color=MUTED):
    return f'<text x="{x}" y="{y}" font-family="monospace" font-size="{size}" fill="{color}">{escape(text)}</text>'

def svg(name, w, h, body, title, motion=False):
    css = '''<style>
    @keyframes arrive { from { opacity:.2; transform:translateY(26px); } to { opacity:1; transform:translateY(0); } }
    @keyframes orbit { from { transform:rotate(-75deg); } to { transform:rotate(0deg); } }
    @keyframes draw { from { stroke-dashoffset:1400; } to { stroke-dashoffset:0; } }
    @keyframes cursor { 0%,45%,85% {opacity:1} 25%,65% {opacity:0} 100%{opacity:1} }
    .intro-a{animation:arrive 1s ease-out both}.intro-b{animation:arrive 1.4s ease-out both}.intro-c{animation:arrive 1.8s ease-out both}
    .orbit{transform-origin:945px 292px;animation:orbit 4.5s cubic-bezier(.16,1,.3,1) both}
    .trace{stroke-dasharray:1400;animation:draw 4s ease-out both}.cursor{animation:cursor 4.5s linear both}
    @media(prefers-reduced-motion:reduce){.intro-a,.intro-b,.intro-c,.orbit,.trace,.cursor{animation:none!important}}
    </style>''' if motion else ''
    (A/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>{css}{body}</svg>\n')

def texture(w,h,bg=INK):
    return f'<defs><pattern id="mesh" width="16" height="16" patternUnits="userSpaceOnUse"><path d="M16 0H0V16" fill="none" stroke="{MUTED}" stroke-width=".45" opacity=".16"/></pattern><pattern id="dots" width="7" height="9" patternUnits="userSpaceOnUse"><circle cx="2" cy="3" r=".55" fill="{INK}" opacity=".2"/></pattern></defs><path fill="{bg}" d="M0 0h{w}v{h}H0z"/><path fill="url(#mesh)" d="M0 0h{w}v{h}H0z"/>'

def arrow(x,y,size=25,color=INK):
    return f'<path d="M{x} {y+size}l{size} -{size}m-{size} 0h{size}v{size}" fill="none" stroke="{color}" stroke-width="4"/>'

hero = texture(1200,570)
hero += '<path fill="#d93b2c" d="M0 0h12v570H0z"/>'
hero += display('PB',36,53,36)+mono('PHILIP JOHN BASILE / INDEPENDENT ENGINEER',104,44,16,PAPER)
hero += mono('NEW ROCHELLE, NY',968,42,13)+ '<path d="M36 73H1164" stroke="#6b655b"/>'
hero += '<g class="intro-a">'+display('MAKE',32,210,145)+'</g>'
hero += '<g class="intro-b">'+display('SOMETHING',32,352,145)+'</g>'
hero += '<g class="intro-c">'+display('MATTER.',32,497,145,RED)+'<path d="M36 511l470 -5 -9 8 -455 4z" fill="#d93b2c"/></g>'
# An exploded record / orbital diagram: decoration, not pretend controls.
hero += '<g opacity=".9"><circle cx="945" cy="292" r="193" fill="#23221f" stroke="#575249"/><circle cx="945" cy="292" r="177" fill="none" stroke="#e8e5dd" stroke-width="2"/><circle cx="945" cy="292" r="155" fill="none" stroke="#575249" stroke-dasharray="2 8"/><circle cx="945" cy="292" r="128" fill="none" stroke="#625e55"/></g>'
hero += '<g class="orbit"><path d="M768 292a177 177 0 0 1 177 -177" fill="none" stroke="#d93b2c" stroke-width="14"/><circle cx="1122" cy="292" r="10" fill="#e8e5dd"/>'
for n in range(36):
    a=n*pi/18
    x1,y1=945+186*cos(a),292+186*sin(a)
    x2,y2=945+193*cos(a),292+193*sin(a)
    hero+=f'<path d="M{x1:.2f} {y1:.2f}L{x2:.2f} {y2:.2f}" stroke="#aaa395"/>'
hero+='</g>'
hero += '<g transform="rotate(-8 945 292)"><path fill="#080807" opacity=".5" d="M827 222h256v159H827z"/><path fill="#e8e5dd" d="M815 210h256v159H815z"/><path fill="url(#dots)" d="M815 210h256v159H815z"/>'+mono('FIELD NOTES / EST. 1998',832,239,13,INK)+display('STILL',831,294,53,INK)+display('CURIOUS.',831,348,53,RED)+'</g>'
hero += '<path class="trace" d="M689 443h59v-63h54M1060 192h65v-65h39" fill="none" stroke="#d93b2c" stroke-width="2"/>'
hero += mono('CODE. CURIOSITY. CONSEQUENCE.',783,507,16,PAPER)
hero += '<path fill="#e8e5dd" d="M12 535H1200V570H12z"/>'+mono('APPLE MLX  /  LOCAL AI  /  REAL-WORLD SYSTEMS',34,558,14,INK)+mono('OPEN THE LAB',963,558,15,INK)
hero += '<path class="cursor" d="M1146 544v15m-6 -6 6 6 6-6" fill="none" stroke="#d93b2c" stroke-width="3"/>'
svg('studio-hero.svg',1200,570,hero,'Philip John Basile — Make something matter. Still curious. Open the project lab below.',True)

mobile=texture(600,610)+display('PHILIP JOHN BASILE',25,58,38)+mono('INDEPENDENT ENGINEER / EST. 1998',27,87,15)
mobile+='<path d="M25 109H575" stroke="#625e55"/>'
mobile+='<g class="intro-a">'+display('MAKE',23,254,143)+'</g><g class="intro-b">'+display('SOMETHING',23,398,133)+'</g><g class="intro-c">'+display('MATTER.',23,544,143,RED)+'</g>'
mobile+='<path fill="#e8e5dd" d="M0 572H600V610H0z"/>'+mono('STILL CURIOUS. / OPEN THE LAB ↓',27,598,19,INK)
svg('studio-hero-mobile.svg',600,610,mobile,'Philip John Basile — Make something matter. Open the project lab below.',True)

for slug,num,title,sub in [('patches','01','THE PATCHES','CONTRIBUTING UPSTREAM'),('lab','02','THE LAB','OPEN A PROJECT'),('notes','03','FIELD NOTES','READ THE WORK'),('hello','04','SAY HELLO','START SOMETHING')]:
    b=texture(580,136,PAPER)
    b+='<path d="M0 128H580V136H0z" fill="#aaa395"/><path d="M0 0h7v128H0z" fill="#d93b2c"/>'
    b+=display(num,20,92,70,RED)+mono(sub,119,36,14,INK)+display(title,115,100,52,INK)+arrow(526,58,22)
    svg(f'nav-{slug}.svg',580,136,b,title+'. '+sub.capitalize()+'.')

for slug,num,eyebrow,title in [('upstream','01','CODE THAT LEFT THE BUILDING','GOOD CODE TRAVELS.'),('work','02','CLICK A COVER. FOLLOW THE THREAD.','OPEN THE LAB.'),('models','03','WEIGHTS / DATA / DEMOS','TAKE IT FOR A SPIN.'),('about','04','THE PERSON BEHIND THE PATCHES','STILL BUILDING.'),('writing','05','NOTES, NULL RESULTS & NEXT QUESTIONS','LEAVE A PAPER TRAIL.')]:
    b=texture(1200,150)
    b+=display(num,20,116,104,RED)+mono(eyebrow,160,34,16)+display(title,155,113,66)
    b+='<path d="M160 137H1190" stroke="#625e55"/>'
    svg(f'studio-{slug}.svg',1200,150,b,f'{num} / {title.capitalize()} {eyebrow.capitalize()}')

def icon(kind,x,y):
    s=f'<g transform="translate({x} {y})">'
    if kind=='code':
        s+='<path d="M0 0h116v90H0z" fill="#242320" stroke="#625e55"/><path d="M0 20H116" stroke="#625e55"/><circle cx="10" cy="10" r="3" fill="#d93b2c"/><circle cx="21" cy="10" r="3" fill="#aaa395"/>'
        s+=mono('def wisp():',9,41,11,PAPER)+mono('return',15,63,13,PAPER)+'<path d="M75 50h8v15H75z" fill="#d93b2c"/>'
    elif kind=='flow':
        s+='<path d="M13 20h93v51H13zM60 20v51" fill="none" stroke="#d93b2c" stroke-width="3"/>'
        for xx,yy in [(0,4),(78,4),(40,56)]:s+=f'<rect x="{xx}" y="{yy}" width="36" height="26" fill="#e8e5dd" stroke="#191918" stroke-width="3"/>'
    elif kind=='layers':
        for yy,c in [(0,'#aaa395'),(25,'#d93b2c'),(50,'#e8e5dd')]:s+=f'<path d="M0 {yy+20}l55 -20 55 20 -55 20z" fill="{c}" stroke="#191918" stroke-width="2"/>'
    else:
        for yy in [0,30,60]:s+=f'<path d="M0 {yy}h112v22H0z" fill="#e8e5dd" stroke="#191918"/>'+f'<path d="M85 {yy+11}l5 5 10-12" fill="none" stroke="#d93b2c" stroke-width="3"/>'
    return s+'</g>'

for slug,num,category,title,desc,kind in [('wisp','01','CODE MODEL / MLX','WISP CODER','FROM TOKENIZER TO RELEASED WEIGHTS','code'),('agents','02','ENTERPRISE / MCP','AGENT SYSTEMS','IDENTITY → TOOLS → REVIEW → ACTION','flow'),('local','03','APPLE SILICON / METAL','LOCAL INFERENCE','RUNTIME / WEIGHTS / MEMORY / STORAGE','layers'),('rag','04','RETRIEVAL / EVALUATION','RAG & RELEASES','RETRIEVE → EVALUATE → RELEASE','eval')]:
    b=texture(1200,200,PAPER)
    b+='<path d="M0 15h270l25 -15h260l22 15H1200V193H0z" fill="#d8d2c5"/><path d="M0 35H1200V193H0z" fill="#e8e5dd"/><path d="M0 35H1200V193H0z" fill="url(#dots)"/><path d="M0 193H1200V200H0z" fill="#a49b8c"/>'
    b+=mono('CASE '+num,24,25,14,INK)+icon(kind,28,69)+mono(category,182,65,17,RED)+display(title,179,130,65,INK)+mono(desc,182,169,15,INK)
    b+='<path d="M1069 69h83v83H1069z" fill="#191918"/><path d="M1094 110h33m-16-16v33" stroke="#e8e5dd" stroke-width="4"/>'
    b+=mono('EXPAND / FOLD',1046,174,13,INK)
    svg(f'case-{slug}.svg',1200,200,b,f'Case {num}: {title.title()}. Expand or fold the project details.')
    m=texture(600,168,PAPER)
    m+='<path d="M0 0h190l18 12H600V22H0z" fill="#c7beaf"/><path d="M0 161H600V168H0z" fill="#a49b8c"/>'
    m+=mono('CASE '+num,15,17,12,INK)+'<g transform="translate(14 63) scale(.66)">'+icon(kind,0,0)+'</g>'
    m+=mono(category,107,54,14,RED)+display(title,105,111,47,INK)+mono('TAP TO EXPAND / FOLD',107,144,15,INK)
    m+='<path d="M543 69h42v42H543z" fill="#191918"/><path d="M553 90h22m-11-11v22" stroke="#e8e5dd" stroke-width="3"/>'
    svg(f'case-{slug}-mobile.svg',600,168,m,f'Case {num}: {title.title()}. Expand or fold the project details.')

b=texture(1200,160,RED)+display('YOUR NEXT CLICK COULD BE A GOOD ONE.',24,88,53,INK)+mono('OPEN THE APPLE SILICON AI COLLECTION',27,130,20,PAPER)+arrow(1120,48,42,PAPER)
svg('launch-hub.svg',1200,160,b,'Launch the Apple Silicon AI collection: models, data, demos, and guides.')
b=texture(1200,190,PAPER)+mono('HAVE SOMETHING WORTH BUILDING?',30,40,18,RED)+display('LET’S MAKE A USEFUL DENT.',27,124,75,INK)+mono('START A CONVERSATION ↗',30,164,18,INK)+arrow(1090,70,55,RED)
svg('studio-contact.svg',1200,190,b,'Let’s make a useful dent. Start a conversation.')
for slug,label in [('wisp','TRY WISP IN YOUR BROWSER'),('agents','EXPLORE THE AGENT PLATFORM'),('local','EXPLORE LOCAL INFERENCE'),('rag','EXPLORE THE RAG SYSTEM')]:
    b=texture(720,88)+display(label,20,58,34)+arrow(665,27,24,RED)
    b+='<path d="M0 81H720V88H0z" fill="#d93b2c"/>'
    svg(f'launch-{slug}.svg',720,88,b,label.title()+'. Opens the live demo or portfolio case study.')
print('Built the studio hero, navigation, headings, project covers, and launch panels.')
