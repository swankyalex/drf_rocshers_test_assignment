[![main](https://github.com/swankyalex/drf_rocshers_test_assignment/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/swankyalex/drf_rocshers_test_assignment/actions)
[![Lines of code](https://img.shields.io/tokei/lines/github/swankyalex/drf_rocshers_test_assignment)](https://github.com/swankyalex/drf_rocshers_test_assignment/tree/master)

![CMake](https://img.shields.io/badge/CMake-%23008FBA.svg?style=for-the-badge&logo=cmake&logoColor=white)
![Python](https://img.shields.io/badge/-Python-orange?logo=python&logoColor=white&style=for-the-badge)&nbsp;
![Pytest](https://img.shields.io/badge/-Pytest-9cf?logo=pytest&logoColor=white&style=for-the-badge)&nbsp;
![Poetry](https://img.shields.io/badge/-poetry-purple?logo=poetry&style=for-the-badge&logoColor=white)&nbsp;
![Django](https://img.shields.io/badge/-Django-green?logo=django&style=for-the-badge&url=https://www.djangoproject.com/)&nbsp;
![REST-API](https://img.shields.io/badge/-RestAPI-9cf?logo=django&style=for-the-badge&url=https://www.djangoproject.com/)&nbsp;
![Docker](https://img.shields.io/badge/-Docker-blue?logo=docker&style=for-the-badge&url=https://www.djangoproject.com/)&nbsp;
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-blue?logo=postgresql&style=for-the-badge&logoColor=white)&nbsp; 
![Gunicorn](https://img.shields.io/badge/-gunicorn-green?logo=gunicorn&style=for-the-badge&logoColor=white)&nbsp;

#### Заданию было уделено ~15 часов. Покрытие кода тестами 100%

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

Также реализована система регистрации и аутентификации пользователей.

Авторизация возможна через сессии либо через токен.

### API

Реализованы эндпоинты:

### Управление станциями
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
  
### Управление учетными записями
* GET, POST: /api/users/profile/
  * Регистрация нового пользователя / получение всех профилей
  * Схемы запроса и ответа совпадают со схемой модели пользователя
  
* GET, PUT, PATCH, DELETE: /api/users/profile/{id}/
  * CRUD пользователей 
  * Схемы запроса и ответа совпадают со схемой модели пользователя

* POST: /api/users/login/
  * Получение токена авторизации для пользователя

### Документация

На основе эндпоинтов генерируется swagger через drf-spectacular. 

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
poetry run python src/manage.py migrate
```

5. Для запуска сервера используйте команду:
```sh
poetry run python src/manage.py runserver 
```

6. Для авторизации создайте суперпользователя:
```sh
poetry run python src/manage.py createsuperuser 
```
либо зарегистрируйтесь по эндпойнту:
**/api/users/profile/**

7. Тестирование приложения происходит через pytest следующими командами:
```sh
poetry run pytest src 
```
8. Покрытие кода тестами через coverage:
```sh
poetry run pytest src --cov 
```

![Results](https://i.ibb.co/dt8cvhX/Screenshot-from-2022-11-20-15-53-07.png)

### Использование через docker (используется база данных PostgreSQL)
1. Склонируйте данный репозиторий на свою локальную машину
2. Выполните команду:
```sh
docker-compose build  
```
затем
```sh
docker-compose up 
```

3. Для авторизации создайте суперпользователя одной из команд
```sh
docker-compose exec web make su 
```

либо зарегистрируйтесь по эндпойнту:
**/api/users/profile/**

## Доступные Make команды

```
make venv           Создание виртуального окружения (poetry install)
make venv-dev       Создание виртуального окружения c dev зависимостями (poetry install --with dev)
make run            Запуск локального сервера (python manage.py runserver)
make run-prod       Запуск сервера через gunicorn
make format         Форматирование кода через black, isort.
make sh             Запуск django shell (python manage.py shell)
make su             Создать суперпользователя (python manage.py createsuperuser)
make migrations     Создание миграций (python manage.py makemigrations)
make migrate        Применение миграций (python manage.py migrate)
make static         Сбор статических файлов (python manage.py collectstatic)
make test           Запуск тестов (pytest src)
make cov            Запуск проверки покрытия кода тестами (pytest src --cov)
make docker         Сборка образа (docker-compose build)
make docker-run     Запуск контейнера (docker-compose up)
make docker-clean   Очистка всех образов приложения
```
