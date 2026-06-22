# LaTeX Business Card

Print-ready, single-page business card (85 × 55 mm, ISO 7810 ID-1) that mirrors the
[web contact card](../index.html):

- Circular headshot, name, title, affiliation, and contact rows on the left.
- A QR code top-right. Scanning it opens your hosted contact card, where the visitor taps
  **Save contact** to download a vCard (and add it to their phone).

## Files

| File           | Purpose                                                    |
| -------------- | --------------------------------------------------------- |
| `card.tex`     | The card. Edit the `EDIT ONLY THIS BLOCK` section.        |
| `Makefile`     | Build helper (`make`, `make qr`, `make clean`).          |
| `headshot.jpg` | Front photo (copied from the repo root).                  |
| `qr.png`       | QR code, generated from your card URL.                    |

## Requirements

- A TeX distribution with `pdflatex` (TeX Live / MiKTeX). Packages used: `geometry`, `tikz`,
  `graphicx`, `helvet`, `fontawesome5`, `xcolor` — all in a standard install.
- For regenerating the QR: Python + `qrcode` (see `../requirements.txt`).

## Build

```sh
make                       # regenerates qr.png, then builds card.pdf
```

Point the QR at a different URL:

```sh
make CARD_URL="https://shinawy.github.io/contact-card/"
```

### Without `make`

```sh
# 1. (optional) regenerate the QR for your hosted card
../.qrenv/bin/python ../make_qr.py https://shinawy.github.io

# 2. build — run TWICE (TikZ 'remember picture' needs the second pass to place elements)
pdflatex card.tex
pdflatex card.tex
```

> **Run pdflatex twice.** The layout uses TikZ `remember picture`/`current page`, whose absolute
> positions are read from the `.aux` file written on the first pass. A single run leaves the card
> nearly blank. `make` already does both passes.

## Customise

Edit the block at the top of `card.tex`:

- `\Name`, `\Title`, `\Affil`
- `\Photo`, `\Qr` — asset filenames
- `\ContactRows` — add/remove `\row{\faIcon}{value}` lines (icons from the `fontawesome5`
  package, e.g. `\faEnvelope`, `\faGlobe`, `\faOrcid`, `\faGithub`, `\faLinkedin`,
  `\faPhone`, `\faTwitter`)
- Colours: `accent`, `ink`, `muted`, `accentsoft` (default accent matches the web card, `#0F5E5A`)

## Printing

- The PDF is exactly 85 × 55 mm — standard business-card size, **no bleed**. If your print shop
  requires bleed, add it in `\geometry` (e.g. `paperwidth=91mm,paperheight=61mm`) and extend the
  background fills.
- Single-sided — print the back blank, or reuse it for anything you like.
- Keep the headshot ≥ 300 dpi (the supplied `headshot.jpg` is high-res).
