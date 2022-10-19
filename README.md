# Проект: Api_final_yatube
***
## Описание:
Проект является продолжением серии проектов по созданию социальной сети Yatube. В данном проекте продолжается изучение API, прав, авторизации, фильтров, поиска, сортировки.


## Установка:
***
1. Клонируйте репозиторий:
```
git clone git@github.com:easyRU/api_final_yatube.git
```
2. Создайте виртуальное окружение:
```
python -m venv env
```
3. Установите зависимости: 
```
pip install -r requirements.txt
```
4. Примените миграции: 
```
python manage.py migrate
```
5. Запустите сервер: 
```
python manage.py runserver
```

## Примеры:
***
```
POST http://127.0.0.1:8000/api/v1/posts/
```

![image](https://user-images.githubusercontent.com/96536178/196784713-b1282977-72a4-4fc9-8867-29f8671e5bec.png)

```
GET http://127.0.0.1:8000/api/v1/posts/1/
```

![image](https://user-images.githubusercontent.com/96536178/196784819-292b6a43-5544-49ea-88a3-fe012e256a56.png)

```
PATCH http://127.0.0.1:8000/api/v1/posts/2/
```

![image](https://user-images.githubusercontent.com/96536178/196788638-2eed500a-8854-40b1-b8cc-60626343d9c4.png)

```
GET http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2 with pagination
```

![image](https://user-images.githubusercontent.com/96536178/196791032-2f040742-8a5d-41f2-a88a-40c645d8c1b4.png)