include ./Makefile.in.mk


.PHONY: format
format:
	$(call log, reorganizing imports & formatting code)
	$(RUN) isort "$(DIR_SRC)" "$(DIR_SCRIPTS)"
	$(RUN) black "$(DIR_SRC)" "$(DIR_SCRIPTS)"
	$(RUN) flake8 "$(DIR_SRC)"
	$(call log, All good!)


.PHONY: run
run:
	$(call log, starting local web server)
	$(PYTHON) src/manage.py runserver


.PHONY: run-prod
run-prod:
	$(call log, starting local web server)
	$(RUN) gunicorn --config="$(DIR_SCRIPTS)/gunicorn.conf.py" $(WSGI_APPLICATION)


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


PHONY: static
static:
	$(call log, collecting static)
	$(PYTHON) src/manage.py collectstatic


.PHONY: test
test:
	$(call log, running tests)
	$(RUN) pytest "$(DIR_SRC)"


.PHONY: cov
cov:
	$(call log, running tests)
	$(RUN) pytest "$(DIR_SRC)" --cov


.PHONY: docker
docker:
	docker-compose build


.PHONY: docker-run
docker-run:
	docker-compose up


.PHONY: docker-clean
docker-clean:
	docker-compose stop || true
	docker-compose down || true
	docker-compose rm --force || true
	docker system prune --force


.PHONY: docker-su
docker-su:
	$(call log, running docker)
	docker-compose exec web poetry run python src/manage.py createsuperuser


wait-for-db:
	$(call log, waiting for DB up)
	$(DIR_SCRIPTS)/wait_for_postgresql.sh \
		$(shell $(PYTHON) $(DIR_SCRIPTS)/get_db_host.py) \
		$(shell $(PYTHON) $(DIR_SCRIPTS)/get_db_port.py) \

