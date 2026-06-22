# Build the business card PDF.
#   make            -> card.pdf (regenerates QR first)
#   make qr         -> regenerate qr.png only
#   make clean      -> remove LaTeX aux files
#   make distclean  -> also remove card.pdf

CARD_URL ?= https://shinawy.github.io
PY       := ../.qrenv/bin/python
TEX      := pdflatex -interaction=nonstopmode -halt-on-error

card.pdf: card.tex qr.png headshot.jpg
	$(TEX) card.tex >/dev/null
	@echo "Wrote card.pdf"

qr: qr.png
qr.png:
	$(PY) ../make_qr.py "$(CARD_URL)"

clean:
	rm -f card.aux card.log card.out

distclean: clean
	rm -f card.pdf

.PHONY: qr clean distclean
