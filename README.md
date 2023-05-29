# Первая задача
## Иструкция по сборке:
### Добавить .env файл с переменными:
``` .env
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DB
```
### Выполнить скрипты
~~~ bash 
cd 1 
~~~
~~~ bash
docker-compose up --build
~~~
## Запросы к API
### Шаблон запроса 
### Пример запроса (POST)
~~~ 
curl -X 'POST' \
  'http://0.0.0.0:8000/questions/?questions_num=3' \
  -H 'accept: application/json' \
  -d ''
~~~

# Задача 2
## Иструкция по сборке:
### Добавить .env файл с переменными:
``` .env
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DB
```
### Выполнить скрипты
~~~ bash 
cd 2
~~~
~~~ bash
docker-compose up --build
~~~
## Запросы к API
### Шаблон запросов
#### Создание пользователя 
~~~ 
curl -X 'POST' \
  'http://0.0.0.0:8000/user/?username=admin' \
  -H 'accept: application/json' \
  -d ''
~~~
####  Добавление аудизописи
~~~ 
curl -X 'POST' \
  'http://0.0.0.0:8000/record?login=admin-e7434784f0b2426&token=226d3b7c-0602-459d-860c-d2b176aa29cd' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'record=@file_example_WAV_1MG.wav;type=audio/x-wav'
~~~
### Получение аудио записи
~~~ 
curl -X 'GET' \
  'http://0.0.0.0:8000/record?id=eb30832b-9c84-4666-b092-ba022c32e7c4&user=admin' \
  -H 'accept: application/json'
~~~
