### О проекте:

Учебный проект API приложения на Django Rest Framework с возможностью отправлять, сообщения, комментировать сообщения, подписываться на сообщения других авторов.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ASTimch/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd api_final_yatube
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

Подробная документация к API проекта: 

```
http://127.0.0.1:8000/redoc/
```
