"""Refine the original studio artwork without changing its kinetic hero.

Build the original assets first, then the joined navigation and connected
section artwork. Requires fonttools; all interaction remains native HTML.
"""
from pathlib import Path
import runpy

base = runpy.run_path(str(Path(__file__).with_name('build-studio-art.py')))
svg, texture, display, mono, arrow = (base[n] for n in ('svg','texture','display','mono','arrow'))
INK, PAPER, RED, MUTED = (base[n] for n in ('INK','PAPER','RED','MUTED'))

# Four linked slices form one paper index, sharing edges and a single baseline.
doors = [('patches','01','THE PATCHES','PATCHES','UPSTREAM CODE'),
         ('lab','02','THE LAB','THE LAB','MODELS & SYSTEMS'),
         ('notes','03','FIELD NOTES','FIELD NOTES','IDEAS & EVIDENCE'),
         ('hello','04','SAY HELLO','SAY HELLO','START SOMETHING')]
for i,(slug,num,title,short,sub) in enumerate(doors):
    for mobile in (False,True):
        h = 222 if mobile else 142
        b=texture(304,h,PAPER)
        b+=f'<path d="M0 {h-5}H304V{h}H0z" fill="{RED}"/>'
        if i: b+=f'<path d="M0 18V{h-23}" stroke="#bbb4a8"/>'
        if mobile:
            b+=display(num,18,76,64,RED)
            words=short.split(' ')
            if len(words)>1:
                b+=display(words[0],18,128,42,INK)+display(' '.join(words[1:]),18,174,42,INK)
            else: b+=display(short,18,146,45,INK)
            b+=arrow(252,174,22,INK)
        else:
            b+=mono(num,20,28,15,RED)+mono(sub,55,28,12,INK)
            b+=display(title,18,98,45,INK)+arrow(268,106,16,RED)
        svg(f'studio-index-{slug}'+('-mobile' if mobile else '')+'.svg',304,h,b,title.title()+'. '+sub.capitalize()+'.')

# The same grid and red spine run through all five headings. A cut paper edge
# softens their transition into native GitHub prose; the bold lettering stays.
sections=[('upstream','01','CODE THAT LEFT THE BUILDING','GOOD CODE TRAVELS.'),
          ('work','02','FROM TOKENIZER TO THE TOOLS A PERSON USES','OPEN THE LAB.'),
          ('about','04','1998 → CREATIVE SYSTEMS → PRODUCTION AI','STILL BUILDING.'),
          ('writing','05','NOTES, NULL RESULTS & NEXT QUESTIONS','LEAVE A PAPER TRAIL.')]
for slug,num,eyebrow,title in sections:
    for mobile in (False,True):
        w,h=(600,144) if mobile else (1200,158)
        # Small irregularities give the original grid a tactile edge.
        clip=f'M0 0H{w}V{h-7}l-42 3 -38-2 -35 3 -28-2 -45 3 -38-2 -30 2H0z'
        b=f'<defs><clipPath id="surface"><path d="{clip}"/></clipPath></defs><g clip-path="url(#surface)">'+texture(w,h)
        b+=f'<path d="M0 0h8v{h}H0z" fill="{RED}"/>'
        if mobile:
            b+=display(num,23,105,83,RED)
            # Mobile wording is shorter while the README alt text is complete.
            brows={'upstream':'CONTRIBUTING UPSTREAM','work':'MODELS / RUNTIMES / AGENTS','about':'BUILDING SINCE 1998','writing':'IDEAS / EVIDENCE / RESULTS'}
            b+=mono(brows[slug],127,31,13,MUTED)+display(title,124,93,40,PAPER)
            b+=f'<path d="M128 116H574" stroke="#625e55"/>'
        else:
            b+=display(num,24,114,98,RED)+mono(eyebrow,158,34,16,MUTED)+display(title,154,110,64,PAPER)
            b+=f'<path d="M158 134H1168" stroke="#625e55"/>'
        b+='</g>'
        svg(f'connected-{slug}'+('-mobile' if mobile else '')+'.svg',w,h,b,num+' / '+title.title())

# One composition replaces the former dark heading plus separate red billboard.
for mobile in (False,True):
    w,h=(600,380) if mobile else (1200,282)
    b=texture(w,h)+f'<path d="M0 0h8v{h}H0z" fill="{RED}"/>'
    if mobile:
        b+=mono('03 / HUGGING FACE',25,34,16,MUTED)
        b+=display('TAKE IT FOR',23,114,68,PAPER)+display('A SPIN.',23,185,68,PAPER)
        b+=mono('20 MODELS / 1 DATASET / 2 SPACES',27,226,16,MUTED)
        b+=f'<path d="M8 256H600V380H8z" fill="{RED}"/>'
        b+=display('OPEN THE LOCAL AI GUIDE',24,311,35,PAPER)+mono('MODELS · DATA · DEMOS · RECIPES',27,348,17,PAPER)+arrow(548,285,24,PAPER)
    else:
        b+=display('03',24,114,98,RED)+mono('HUGGING FACE / APPLE SILICON',158,34,16,MUTED)+display('TAKE IT FOR A SPIN.',154,110,64,PAPER)
        b+=mono('ORIGINAL MODELS → CONVERSIONS → RUNTIMES → LIVE DEMOS',159,153,17,MUTED)
        b+=f'<path d="M8 189H1200V282H8z" fill="{RED}"/>'
        b+=display('OPEN THE LOCAL AI GUIDE',27,248,44,PAPER)+mono('20 MODELS / 1 DATASET / 2 SPACES',696,240,17,PAPER)+arrow(1135,217,30,PAPER)
    svg('connected-models'+('-mobile' if mobile else '')+'.svg',w,h,b,'03 / Take it for a spin. Open the Local AI Guide: 20 models, 1 dataset, 2 Spaces. Snapshot September 11, 2026.')

print('Built the joined paper index and studio section artwork. Original hero unchanged.')
