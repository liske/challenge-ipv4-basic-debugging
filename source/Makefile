# Minimal makefile for Sphinx documentation
#

langs         = en de

all: html
	

html: $(foreach lang,$(langs),html-$(lang))
	

html-%: $(SPHINX_DEPENDENCIES)
	cd $* && make html
