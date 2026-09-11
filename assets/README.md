# Profile artwork

Adapted from the live street-art edition of [philipjohnbasile.com](https://philipjohnbasile.com/).

- Palette: paper `#e8e5dd`, ink `#191918`, red `#b7251d`.
- Original mural: `static/assets/open-code-stencil-mural.png` in [the website source](https://github.com/PhilipJohnBasile/philipjohnbasile.com/tree/7ab23b58224789f211e41fd38f95c9922e2585a3). Embedded unchanged in the desktop hero SVG.
- Anton: Copyright 2020 The Anton Project Authors. Included under the SIL Open Font License in [ANTON-OFL.txt](ANTON-OFL.txt). Display lettering is converted to paths so GitHub can show the same typography without loading an external font.
- Every SVG is self-contained. No scripts, external image services, or remote font requests are needed.
- The narrow-screen hero uses the same lettering, with normal README text retaining the readable introduction, links, and project descriptions.

To rebuild, install `fonttools` and run `python3 scripts/build-profile-art.py` from the repository root. Edit the text and geometry in that script; generated SVGs are committed for GitHub to display directly.

GitHub controls the page background, typography of ordinary text, tables, and navigation. Images carry the website’s visual identity; semantic headings, links, and expandable details keep the profile usable in GitHub’s native layout.
