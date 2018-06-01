
#Makefile for latex

TEX = paper
TARGET = $(TEX).pdf
TARGETPS = $(TEX).ps
TARGETEXTRA = review_response.pdf

SOURCES = $(wildcard *.tex)
BIBFILE  = $(wildcard *.bib)

LATEX = latex
BIBTEX = bibtex -min-crossrefs=1000
GREP = egrep
DVIPS = dvips
DVIPSFLAGS = -t Letter -Ppdf -G0 
PS2PDF = ps2pdf
PS2PDFFLAGS = -sPAPERSIZE=letter -dCompatibilityLevel=1.4 -dEmbedAllFonts=true -dPDFSETTINGS=/prepress


all: $(TARGET) check 
#$(TARGETEXTRA)

pdf:	$(TEX).pdf check
ps:	$(TEX).ps check
review: $(TARGETEXTRA)

ps2pdf:
	$(PS2PDF) $(PS2PDFFLAGS) $(TEX).ps

$(TARGET): $(SOURCES) $(BIBFILE)
$(TARGETPS): $(SOURCES) $(BIBFILE)

%.pdf: %.tex
	pdflatex $*
	$(BIBTEX) $*
	pdflatex $*
	pdflatex $*
	@echo "\n## Make sure that your 'pdflatex' is configured to 'Letter' size paper. (use sudo texconfig-sys)\n"

#%.pdf: $(SOURCES) %.bbl
#%.pdf: %.ps 
#	$(PS2PDF) $(PS2PDFFLAGS) $*.ps
#
#%.ps: %.dvi
#	$(DVIPS) -o $*.ps $(DVIPSFLAGS) $*.dvi
#
#%.dvi: %.tex 
#	$(LATEX) $*
#	$(GREP) -c "No file.*\.bbl|Citation.*undefined" $*.log && $(BIBTEX) $* ; true
#	$(LATEX) $*  
#	$(LATEX) $*
#
#%.bbl: %.aux $(BIBFILE)
#	$(BIBTEX) $*
#
#%.aux: $(SOURCES)
#	$(LATEX) $*
#
check:
	@echo "\n########################################\n"
	@echo "\n## Checking for errors....\n"
	cat $(TEX).log | grep -i "no file\|undefined\|error\|Output written on"
	@echo "\n## Error check done.\n"
	@echo "\n########################################\n"

clean:
	-rm -f *~ *.log *.aux *.bbl *.blg *.idx *.dvi *.lof
	-rm -f *.lot *.ilg *.ind *.toc *.out *.thm
	-rm -f $(TARGET) $(TARGETPS) $(TARGETEXTRA)

