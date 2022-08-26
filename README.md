# api_yatube

### Описание

Проект api_yatube позволяет делать запросы к Yatube и получать запрошенные данные.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Tchuprow/api_yatube
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```


### Примеры запросов:
Получение публикаций: 

```
GET http://127.0.0.1:8000/api/v1/posts/
```

Создание публикации: 

```
POST http://127.0.0.1:8000/api/v1/posts/
```

Получение публикации: 
```
GET http://127.0.0.1:8000/api/v1/posts/{id}/
```

Обновление публикации:

```
PUT http://127.0.0.1:8000/api/v1/posts/{id}/
```

Частичное обновление публикации:

```
PATCH http://127.0.0.1:8000/api/v1/posts/{id}/
```

Удаление публикации:

```
DELETE http://127.0.0.1:8000/api/v1/posts/{id}/
```

Получение комментариев: 

```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Добавление комментария:

```
POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Получение комментария:

```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

Обновление комментария:

```
PUT http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

Частичное обновление комментария:

```
PATCH http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

Удаление комментария:

```
DELETE http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

Список сообществ:

```
GET http://127.0.0.1:8000/api/v1/groups/
```

Iнформация о сообществе:

```
GET http://127.0.0.1:8000/api/v1/groups/{id}/
```

Подписки:

```
GET http://127.0.0.1:8000/api/v1/follow/
```

Подписаться:

```
POST http://127.0.0.1:8000/api/v1/follow/
```

Получить JWT-токен:

```
POST http://127.0.0.1:8000/api/v1/jwt/create/
```

Обновить JWT-токен:
```
POST http://127.0.0.1:8000/api/v1/jwt/refresh/
```

Проверить JWT-токен:

```
POST http://127.0.0.1:8000/api/v1/jwt/verify/
```



