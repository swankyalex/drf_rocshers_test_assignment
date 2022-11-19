include ./Makefile.in.mk


.PHONY: format
format:
	$(call log, reorganizing imports & formatting code)
	$(RUN) isort "$(DIR_SRC)"
	$(RUN) black "$(DIR_SRC)"
	$(RUN) flake8 "$(DIR_SRC)"
	$(call log, All good!)


.PHONY: run
run:
	$(call log, starting local web server)
	$(PYTHON) src/manage.py runserver


.PHONY: sh
sh:
	$(call log, starting Python shell)
	$(PYTHON) src/manage.py shell


.PHONY: venv
venv:
	$(call log, installing packages)
	$(POETRY_INSTALL)


.PHONY: venv-dev
venv-dev:
	$(call log, installing development packages)
	$(POETRY_INSTALL) --with dev


.PHONY: su
su:
	$(call log, starting Python shell)
	$(PYTHON) src/manage.py createsuperuser


.PHONY: migrations
migrations:
	$(call log, generating migrations)
	$(PYTHON) src/manage.py makemigrations


.PHONY: migrate
migrate:
	$(call log, applying migrations)
	$(PYTHON) src/manage.py migrate


.PHONY: test
test:
	$(call log, running tests)
	pytest "$(DIR_SRC)"


.PHONY: cov
cov:
	$(call log, running tests)
	pytest "$(DIR_SRC)" --cov

