# Minimal makefile for Sphinx documentation
#

langs         = en de

all: clean html
	

clean:
	for lang in $(langs); do rm -rf "../docs/($lang)"; done

html: $(foreach lang,$(langs),html-$(lang))
	

html-%: $(SPHINX_DEPENDENCIES)
	cd $* && make html
