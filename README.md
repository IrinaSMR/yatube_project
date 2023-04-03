# yatube_project

# Социальная сеть для блогеров

## _Описание_
> Благодаря этой социальной сети *блогеры* смогут общаться между собой делиться своими идеями, мыслями и оценивать работы друг друга.

## _Технологии_
- Django 2.2.19
- Python 3.10.2

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/IrinaSMR/yatube_project
cd yatube_project
```

Cоздать и активировать виртуальное окружение:
```
python -m venv env
source venv/Scripts/activate
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Для запуска проекта требуется перейти в папку с файлом manage.py и выполнить миграции:
```
python manage.py migrate
```

После чего запустить проект:
```
python manage.py runserver
```

### Автор
Смирнова Ирина
