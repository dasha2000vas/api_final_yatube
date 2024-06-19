# api_yatube

api_yatube - это API для размещения постов и комментариев к ним. Этот сервис позволит людям из разных уголков мира обмениваться информацией, а также делиться своим мнением о ней.

В финальной версии появилась возможность подписываться на других пользователей, а также добавлять фотографии к постам.

## Как скачать и запустить проект:

**1 клонировать в нужную папку**
```
git clone git@github.com:dasha2000vas/api_final_yatube.git
```

**2 создать и активировать виртуальное окружение**
```
python -m venv venv
```
```
source venv/Scripts/activate
```

**3 установить зависимости из файла requirements.txt**
```
pip install -r requirements.txt
```

**4 перейти в папку yatube_api**
```
cd yatube_api/
```

**5 выполнить миграции**
```
python manage.py migrate
```

**6 запустить проект на локальном сервере**
```
python manage.py runserver
```

## Примеры запросов:

url: http://127.0.0.1:8000/api/v1/posts/

### GET-запрос

Response

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### POST-запрос

Request

```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Response

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

## Использованные технологии

Проект создан с помощью приложения VSCode на языке Python. Импортированы следующие пакеты: django, djangorestframework.

## Автор:

* Василевская Дарья
* GitHub: https://github.com/dasha2000vas
* Телеграм: https://t.me/vasdascha
* Почта: vasilevsckaya.dascha@yandex.ru

