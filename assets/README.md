# Profile artwork

The current studio edition adds a short kinetic introduction, section navigation, and project covers that unfold with GitHub's native `details` / `summary` controls. Each open project has a real demo or case-study link. The mobile hero and project covers use `picture` sources.

Rebuild the current edition with `python3 scripts/build-studio-art.py` (requires `fonttools`). Its SVGs contain no scripts or external resources. CSS motion stops within 4.5 seconds and is disabled by `prefers-reduced-motion`; the layout and every link remain usable without animation.

The `picture` wrappers inside project summaries are intentional: they stop GitHub from automatically linking the cover image to its image viewer, which would intercept the click intended to expand the project.

The original street-art edition and its build script are retained below as source material.

Adapted from the live street-art edition of [philipjohnbasile.com](https://philipjohnbasile.com/).

- Palette: paper `#e8e5dd`, ink `#191918`, red `#b7251d`.
- Original mural: `static/assets/open-code-stencil-mural.png` in [the website source](https://github.com/PhilipJohnBasile/philipjohnbasile.com/tree/7ab23b58224789f211e41fd38f95c9922e2585a3). Embedded unchanged in the desktop hero SVG.
- Anton: Copyright 2020 The Anton Project Authors. Included under the SIL Open Font License in [ANTON-OFL.txt](ANTON-OFL.txt). Display lettering is converted to paths so GitHub can show the same typography without loading an external font.
- Every SVG is self-contained. No scripts, external image services, or remote font requests are needed.
- The narrow-screen hero uses the same lettering, with normal README text retaining the readable introduction, links, and project descriptions.

To rebuild, install `fonttools` and run `python3 scripts/build-profile-art.py` from the repository root. Edit the text and geometry in that script; generated SVGs are committed for GitHub to display directly.

GitHub controls the page background, typography of ordinary text, tables, and navigation. Images carry the website’s visual identity; semantic headings, links, and expandable details keep the profile usable in GitHub’s native layout.
