<a id="anchor"></a>
# Scrapy parser PEP
## Описание:
Асинхронный парсер документов PEP на базе фреймворка Scrapy.
Парсер выводит собранную информацию в два файла .csv:
1. В первый файл выводит список всех PEP: номер, название и статус.
2. Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе. 
   В последней строке общее количество всех документов.
   
## Используемые технологии:
Python, Scrapy
   
## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AndreyFilippovich/scrapy_parser_pep.git
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

* Если у вас Linux/MacOS

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

* Если у вас Windows

    ```
    python -m venv venv
    source venv/Scripts/activate
    ```

Установить зависимости из файла `requirements.txt`:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Запуск парсера:

```
scrapy crawl pep
```

Файды будут созданы в дериктории `results`

### Автор проекта:

Филиппович А.В.