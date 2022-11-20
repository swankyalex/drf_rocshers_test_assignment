[![main](https://github.com/swankyalex/drf_rocshers_test_assignment/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/swankyalex/drf_rocshers_test_assignment/actions)
[![Lines of code](https://img.shields.io/tokei/lines/github/swankyalex/drf_rocshers_test_assignment)](https://github.com/swankyalex/drf_rocshers_test_assignment/tree/master)

#### Заданию было уделено ~12 часов. Покрытие кода тестами 100%

# Тестовое задание

Python developer в команду https://www.linkedin.com/in/rocshers/

## Стек

Python, Django, DRF, coverage, OpenAPI, Docker, Docker-compose, PostgreSQL. 


## Приложение

Сервис по управлению космическими станциями.

В сервисе хранится информация станциях и их позиции в пространстве. Через сервис можно CRUD станций и изменять из позицию.

У станции 3 координаты: x, y, z. При запуске станции ее координаты по умолчанию равны: 100, 100, 100.
Станция исправно может двигаться только в диапазоне положительных координат. Если Станция вышла за эти координаты, мы считаем ее неисправной, даже если в будущем она вернулась обратно в разрешенную зону.

Позиция станции меняется через Указание: ось и значение смещения. За одно Указание можно сместиться только в одну сторону на неограниченное расстояние.
Например:
Указание #1: ось: x, смещение: -100. После получения этого указания станция сдвинется по оси X на 100 в лево 

### API

Реализованы эндпоинты:

* GET, POST: /stations/
	* Схемы запроса и ответа совпадают со схемой модели "Станция".
* GET, PUT, PATCH, DELETE: /stations/{station_id}/
	* Схемы запроса и ответа совпадают со схемой модели "Станция".
* GET: /stations/{station_id}/state/ - Получение координат станции.
	* Схема ответа - позиция станции в пространстве:
		* x: int
		* y: int
		* x: int
* POST: /stations/{station_id}/state/ - Изменение позиции станции.
	* Схема запроса совпадает со схемой модели "Указание".
	* Схема ответа - позиция станции в пространстве:
		* x: int
		* y: int
		* x: int

### Документация

На основе эндпоинтов генерируется swagger. 

# Использование
### Без docker (используется база данных SQlite)
1. Склонируйте данный репозиторий на свою локальную машину
2. Убедитесь, что у вас установлен пакет [Poetry](https://python-poetry.org/docs/)
3. Установите зависимости командой:
```sh
poetry install # или poetry install --with dev (для зависимостей разработки)
```
4. Примените миграции:
```sh
poetry run python src/manage.py makemigrations
```
либо
```sh
make makemigrations
```
5. Для запуска сервера используйте команду:
```sh
poetry run python src/manage.py runserver # либо make run
```

6. Для авторизации создайте суперпользователя:
```sh
poetry run python src/manage.py createsuperuser # либо make su
```

7. Тестирование приложения происходит через pytest следующими командами:
```sh
poetry run pytest src # либо make test
```
8. Покрытие кода тестами через coverage:
```sh
poetry run pytest src --cov # либо make cov
```

![Results](https://i.ibb.co/dt8cvhX/Screenshot-from-2022-11-20-15-53-07.png)

### Использование через docker (используется база данных PostgreSQL)
1. Склонируйте данный репозиторий на свою локальную машину
2. Выполните команду:
```sh
docker-compose up -d
```
либо
```sh
make docker-up
```
После окончания билда приложения перейдите на страницу http://127.0.0.1:8000/
3. Для авторизации создайте суперпользователя одной из команд
```sh
docker-compose exec web make su
```
либо
```sh
make docker-su
```
