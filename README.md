# api_yatube - CRUD для Yatube

##CRUD для Yatube

CRUD (сокр. от англ. create, read, update, delete — «создать, прочесть, обновить, удалить») — акроним, обозначающий четыре базовые функции, используемые при работе с персистентными хранилищами данных:
* создание;
* чтение;
* редактирование;
* удаление.

### api_yatube - CRUD для Yatube

Для взаимодействия с ресурсами опишите и настройте такие эндпоинты:
- api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.
- api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
- api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
- api/v1/groups/ (GET): получаем список всех групп.
- api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
- api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
- api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.

### Настройка и запуск на ПК

Клонируем проект:

```bash
git clone https://github.com/oleiip/api_yatube.git
```

или

```bash
git clone git@github.com:oleiip/api_yatube.git
```

Переходим в папку с проектом:

```bash
cd api_yatube
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/Scripts/activate
```

> Для деактивации виртуального окружения выполним (после работы):
> ```bash
> deactivate
> ```
Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python yatube_api/manage.py makemigrations
```
```bash
python yatube_api/manage.py migrate
```

Создаем супер пользователя:

```bash
python yatube_api/manage.py createsuperuser
```

При желании делаем коллекцию статики:

```bash
python yatube_api/manage.py collectstatic
```

Предварительно сняв комментарий с:
```bash
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

И закомментировав: 
```bash
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

Иначе получим ошибку: You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path.

В папку с проектом, где файл settings.py добавляем файл .env куда прописываем наши параметры:

```bash
SECRET_KEY='Ваш секретный ключ'
ALLOWED_HOSTS='127.0.0.1, localhost'
DEBUG=True
```

Не забываем добавить в .gitingore файлы:

```bash
.env
.venv
```

Для запуска тестов выполним:

```bash
pytest
```

Запускаем проект:

```bash
python yatube_api/manage.py runserver localhost:80
```

После чего проект будет доступен по адресу http://localhost/

Заходим в http://localhost/admin и создаем посты, группы, комментарии.
Тестировать и добавлять данные удобно посkе прохождения авторизации через Postman.

