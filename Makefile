VIRTENV = penv
PACKAGE = wrdscli
PYTHON = python
PIP = $(PYTHON) -m pip

$(VIRTENV):
	rm -rf $(VIRTENV)
	virtualenv -p $(PYTHON) $(VIRTENV)
	. $(VIRTENV)/bin/activate; $(PIP) install -e .

dist:
	$(PYTHON) setup.py sdist

develop: $(VIRTENV)
	. $(VIRTENV)/bin/activate; $(PIP) install pylint && $(PIP) install -e .

clean:
	rm -rf $(VIRTENV) dist $(PACKAGE).egg-info
	find . -name '*.pyc' -delete
