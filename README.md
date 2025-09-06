# Пульт охраны банка

Используя этот сайт охраник банка сможет видеть посещения хранилища, все активные карты доступа и их владельцев

## Как установить

Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```
## Подготовка файла .env

В папке проекта создайте файл .env. Заполните переменные `HOST`, `PORT`, `NAME`, `USER`, `PASSWORD`. В настройке `ALLOWED_HOSTS` укажите через запятую, какие хосты смогут обслуживать этот сайт. Настройте `DEBAG-режим` под себя - Тгue или False.

Выглядеть должно примерно так: 

```
DEBUG=False
ENGINE=django.db.backends.postgresql_psycopg2
HOST=checkpoint.devman.org
PORT=5434
NAME=checkpoint
USER=guard
PASSWORD=''
SECRET_KEY=''
ALLOWED_HOSTS=''
```
## Запуск 

Для запуска сервера используйте команду в папке проекта:

```
python manage.py runserver
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
