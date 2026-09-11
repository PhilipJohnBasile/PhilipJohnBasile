"""Build self-contained GitHub artwork. Requires fonttools; no remote renderers.

The existing website mural is embedded unchanged. Anton glyphs become SVG paths
so GitHub does not need to load a webfont or allow custom README CSS.
"""
from base64 import b64encode
from html import escape
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.roundingPen import RoundingPen

ROOT = Path(__file__).resolve().parents[1]
A = ROOT / "assets"
FONT = TTFont(A / "anton-regular.ttf")
GLYPHS = FONT.getGlyphSet()
CMAP = FONT.getBestCmap()
UNITS = FONT["head"].unitsPerEm
INK, PAPER, RED = "#191918", "#e8e5dd", "#b7251d"

def display(text, x, y, size, color=INK):
    paths = []
    cursor = 0
    for char in text:
        name = CMAP[ord(char)]
        pen = SVGPathPen(GLYPHS)
        GLYPHS[name].draw(RoundingPen(pen, roundFunc=lambda n: round(n, 2)))
        paths.append(f'<path transform="translate({cursor} 0)" d="{pen.getCommands()}"/>')
        cursor += GLYPHS[name].width
    scale = size / UNITS
    return f'<g fill="{color}" transform="translate({x} {y}) scale({scale} {-scale})">'+''.join(paths)+'</g>'

def mono(text, x, y, size=15, color=INK):
    return f'<text x="{x}" y="{y}" font-family="monospace" font-size="{size}" fill="{color}">{escape(text)}</text>'

def svg(name, width, height, content, title):
    (A / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>{content}</svg>\n')

def paper(w, h):
    return f'<defs><pattern id="grain" width="9" height="11" patternUnits="userSpaceOnUse"><circle cx="2" cy="3" r=".55" fill="#615d55" opacity=".15"/><circle cx="7" cy="9" r=".3" fill="#615d55" opacity=".12"/></pattern></defs><path fill="{PAPER}" d="M0 0h{w}v{h}H0z"/><path fill="url(#grain)" d="M0 0h{w}v{h}H0z"/>'

mural = b64encode((A / 'open-code-stencil-mural.png').read_bytes()).decode()
hero = paper(1200, 660)
hero += '<path d="M40 86H1160" stroke="#191918" stroke-width="2"/>'
hero += '<g transform="rotate(-5 64 45)"><path fill="#b7251d" d="M43 24h46v48H43z"/><path fill="#191918" d="M39 20h46v48H39z"/>'+display('PB', 47, 57, 31, PAPER)+'</g>'
hero += display('PHILIP JOHN BASILE', 103, 48, 26)+mono('AI ENGINEER & OPEN-SOURCE CONTRIBUTOR', 105, 69, 11)
hero += mono('NEW ROCHELLE, NY / BUILDING SINCE 1998', 789, 50, 11)
hero += mono('INDEPENDENT ENGINEER. OPEN-SOURCE INSTIGATOR.', 43, 131, 13, '#5e332c')
hero += display('MAKE', 39, 259, 130)+display('SOMETHING', 39, 391, 130)
hero += '<g transform="rotate(-3 40 518)">'+display('MATTER.', 39, 524, 130, RED)+'<path fill="#b7251d" d="M43 540l421 -5 -7 8 -403 6z"/></g>'
hero += '<g transform="rotate(2 933 347)"><path fill="#c9c3b7" d="M749 112h373v487H749z"/><path fill="#dbd5c9" d="M742 105h373v487H742z"/>'
hero += f'<image x="752" y="115" width="353" height="441" xlink:href="data:image/png;base64,{mural}"/>'
hero += mono('BUILT IN THE OPEN. SHARED PROGRESS.', 757, 579, 11)
hero += '<path fill="#c5bda8" opacity=".75" d="M790 92l90 -5 2 28 -89 4z"/>'
hero += '<g transform="rotate(-11 823 270)"><path d="M771 210h139v133H771z" fill="none" stroke="#b7251d" stroke-width="3"/>'+display('IDEAS', 783, 250, 37, RED)+display('BELONG', 783, 288, 37, RED)+display('OUT HERE.', 783, 326, 37, RED)+'</g></g>'
hero += '<path fill="#191918" d="M0 607l1200 -7v60H0z"/>'
for x, word in [(39,'OPEN CODE'),(278,'LOCAL INTELLIGENCE'),(635,'REAL-WORLD SYSTEMS'),(1018,'LEAVE A TRAIL')]:
    hero += display(word, x, 640, 25, PAPER)
for x in [238, 595, 976]:
    hero += mono('*', x, 646, 42, '#e94736')
svg('profile-hero.svg', 1200, 660, hero, 'Philip John Basile — Make something matter. Open code, local intelligence, real-world systems. Original website mural of a maker releasing paper birds.')

mobile = paper(600, 570)+display('PHILIP JOHN BASILE', 28, 55, 31)+mono('AI ENGINEER / OPEN-SOURCE CONTRIBUTOR',28,83,13)
mobile += '<path d="M28 104H572" stroke="#191918" stroke-width="2"/>'
mobile += display('MAKE',25,236,130)+display('SOMETHING',25,371,130)
mobile += display('MATTER.',25,506,130,RED)+'<path fill="#b7251d" d="M28 521l418 -4 -6 7 -402 5z"/>'
svg('profile-hero-mobile.svg',600,570,mobile,'Philip John Basile — AI engineer and open-source contributor. Make something matter.')

for filename, number, eyebrow, title in [
 ('upstream','01','CONTRIBUTING UPSTREAM','GOOD CODE TRAVELS.'),
 ('work','02','SELECTED WORK','LESS TALK. MORE BUILT.'),
 ('models','03','MODELS, DATA & DEMOS','LOCAL AI. SHARED PROGRESS.'),
 ('about','04','THE PERSON BEHIND THE PATCHES','STILL BUILDING. STILL QUESTIONING.'),
 ('writing','05','NOTES FROM THE WORK','LEAVE A PAPER TRAIL.')]:
    body = paper(1200,150)+mono(number+' / '+eyebrow,29,35,16,RED)+display(title,27,111,57)
    body += '<path d="M28 137H1172" stroke="#191918" stroke-width="2"/>'
    svg(f'section-{filename}.svg',1200,150,body,number+' / '+eyebrow.title()+'. '+title.capitalize())

body = '<path fill="#191918" d="M0 0h1200v177H0z"/>'+mono('YOUR MOVE / LET’S BUILD SOMETHING USEFUL',30,36,16,'#ed7362')
body += display('LET’S MAKE A USEFUL DENT.',28,116,70,PAPER)+mono('START A CONVERSATION →',30,155,16,PAPER)
svg('contact.svg',1200,177,body,'Let’s make a useful dent. Start a conversation.')
print('Built 8 self-contained SVG assets.')
