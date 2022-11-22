from multiprocessing import cpu_count

from dynaconf import settings as _ds

from scripts.utils import get_setting
from src.project.settings import DIR_SRC

_port = get_setting("PORT", 8000, convert=int)
bind = f"0.0.0.0:{_port}"
chdir = DIR_SRC.as_posix()
graceful_timeout = 10
max_requests = 200
max_requests_jitter = 20
pythonpath = DIR_SRC.as_posix()
loglevel = _ds.GUNICORN_LOGGING
reload = False
timeout = 30
workers = get_setting("WEB_CONCURRENCY", cpu_count() * 2 + 1, convert=int)
