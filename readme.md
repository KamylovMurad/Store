# API для учета визитов сотрудников в торговые точки

Это API позволяет полевым сотрудникам регистрировать свои визиты в торговые точки через мобильное приложение. Работники могут получать список торговых точек, привязанных к их номеру телефона, и регистрировать посещения в эти точки с указанием времени и координат.

## Начало работы

Для запуска проекта  выполните следующие шаги.


1. Создайте файл .env в корневой директории:
```bash 
DEBUG=1
SECRET_KEY=<ваш_секретный_ключ>
POSTGRES_DB=<имя_вашей_бд>
POSTGRES_USER=<пользователь_бд>
POSTGRES_PASSWORD=<пароль_пользователя_бд>
```
2. Установите зависимости

## Административная панель
Перейдите по адресу http://127.0.0.1:8000/admin/, предварительно создав суперпользователя, и войдите, чтобы управлять сущностями Работник, Торговая точка и Посещение.
### Версия Python
- Python 3.11