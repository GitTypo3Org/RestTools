SOURCES          = manual.rst
SOURCES         += manual.tex

RSTLATEX         = rst2latex.py
PDFLATEX         = pdflatex

RSTLATEX_OPTIONS = --no-section-numbering --stylesheet=lmodern --documentclass=sphinxtypo3manual
PDFLATEX_OPTIONS = -interaction=nonstopmode

BASENAME         = manual
GOALS            = manual.pdf

.SECONDARY:

all:
	make -i $(GOALS)
	sleep 1
	touch $(SOURCES)
	make $(GOALS)

%.tex: %.rst
	$(RSTLATEX) $(RSTLATEX_OPTIONS) $< $@

%.pdf: %.tex
	$(PDFLATEX) $(PDFLATEX_OPTIONS) $< $@

clean:
	rm -f $(BASENAME).{aux,log,out,pdf,tex,toc}
