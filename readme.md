# API для учета визитов сотрудников в торговые точки

Это API позволяет полевым сотрудникам регистрировать свои визиты в торговые точки через мобильное приложение. Работники могут получать список торговых точек, привязанных к их номеру телефона, и регистрировать посещения в эти точки с указанием времени и координат.

## Начало работы

Для запуска проекта  выполните следующие шаги.


1. Создайте файл .env в корневой директории:
```bash 
DB_HOST=host
DB_PORT=port
DB_NAME=db_name
DB_USER=username
DB_PASSWORD=password
DJANGO_DEBUG=1
DJANGO_SECRET_KEY=KEY
DJANGO_ALLOWED_HOSTS=ALLOWED_HOSTS
```
2. Установите зависимости

## Административная панель
Перейдите по адресу http://127.0.0.1:8000/admin/, предварительно создав суперпользователя, и войдите, чтобы управлять сущностями Работник, Торговая точка и Посещение.

## Конечные точки API
- `GET api/stores/phone_number/`: Получить список Торговых точек привязанных к переданному номеру телефона.
- `POST api/visits/phone_number/`: Выполнить посещение в Торговую точку.

### Версия Python
- Python 3.11