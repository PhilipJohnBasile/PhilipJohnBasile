# Profile artwork

The current fieldbook edition uses transparent artwork and an open typographic layout. It takes its continuous reading flow from the [Wisp model card](https://huggingface.co/philipjohnbasile/wisp-coder-110m), with the personal site's Anton lettering and red accents. There are no background panels between sections.

Rebuild with `python3 scripts/build-fieldbook-art.py` (requires `fonttools`). Desktop/mobile and light/dark variants are self-contained SVGs. The `picture` sources follow GitHub's theme and viewport. Motion finishes within 3.8 seconds and respects `prefers-reduced-motion`.

The hero itself is a native disclosure: clicking it or pressing Enter reveals the connections from data through models, runtimes, agents, and people, with links to real work. Project titles and career chapters also unfold. Animation provides the introduction; disclosure and navigation are the supported interaction. GitHub does not permit page scripts, custom page styles, or interactive SVG internals inside README image elements.

The `picture` wrappers inside project summaries are intentional: they stop GitHub from automatically linking the cover image to its image viewer, which would intercept the click intended to expand the project.

Earlier studio and street-art assets and their build scripts are retained as source material; they are not loaded by the current README.

Adapted from the live street-art edition of [philipjohnbasile.com](https://philipjohnbasile.com/).

- Palette: paper `#e8e5dd`, ink `#191918`, red `#b7251d`.
- Original mural: `static/assets/open-code-stencil-mural.png` in [the website source](https://github.com/PhilipJohnBasile/philipjohnbasile.com/tree/7ab23b58224789f211e41fd38f95c9922e2585a3). Embedded unchanged in the desktop hero SVG.
- Anton: Copyright 2020 The Anton Project Authors. Included under the SIL Open Font License in [ANTON-OFL.txt](ANTON-OFL.txt). Display lettering is converted to paths so GitHub can show the same typography without loading an external font.
- Every SVG is self-contained. No scripts, external image services, or remote font requests are needed.
- The narrow-screen hero uses the same lettering, with normal README text retaining the readable introduction, links, and project descriptions.

To rebuild, install `fonttools` and run `python3 scripts/build-profile-art.py` from the repository root. Edit the text and geometry in that script; generated SVGs are committed for GitHub to display directly.

GitHub controls the page background, typography of ordinary text, tables, and navigation. Images carry the website’s visual identity; semantic headings, links, and expandable details keep the profile usable in GitHub’s native layout.
