# Minimal makefile for Sphinx documentation
#

langs         = en de

all: clean build	

clean:
	for lang in $(langs); do rm -rf "../docs/($lang)"; done

build: $(foreach lang,$(langs),build-$(lang))
	
build-%: $(SPHINX_DEPENDENCIES)
	cd $* && make html latexpdf epub
