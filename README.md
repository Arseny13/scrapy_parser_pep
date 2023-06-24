# scrapy_parser_pep

<h4>Автор:</h4>

**Изимов Арсений**  - студент Яндекс.Практикума Когорта 17+
https://github.com/Arseny13


<h2>Техническое описание проекта</h2>
Парсер должен выводить собранную информацию в два файла .csv:

-   В первый файл нужно вывести список всех PEP: номер, название и статус
-   Второй файл должен содержать сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). В последней строке этого файла в колонке «Статус» должно стоять слово Total, а в колонке «Количество» — общее количество всех документов.


<h2>Как использовать</h2>
Активировать виртуальное окружение: `python -m venv venv`
Установить зависимости из requirements.txt : `pip install - r requirements.txt`
Запустить паука: `scrapy crawl pep`
Результат работы появится в папке `results` в формате 2х csv файлов.

<h2>Используемые технологии</h2>

- attrs==21.4.0
- Automat==20.2.0
- cffi==1.15.0
- constantly==15.1.0
- cryptography==36.0.2
- cssselect==1.1.0
- h2==3.2.0
- hpack==3.0.0
- hyperframe==5.2.0
- hyperlink==21.0.0
- idna==3.3
- importlib-metadata==4.2.0
- incremental==21.3.0
- iniconfig==1.1.1
- itemadapter==0.4.0
- itemloaders==1.0.4
- jmespath==1.0.0
- lxml==4.9.2
- mccabe==0.6.1
- packaging==21.3
- parsel==1.6.0
- pluggy==1.0.0
- priority==1.3.0
- Protego==0.2.1
- py==1.11.0
- pyasn1==0.4.8
- pyasn1-modules==0.2.8
- pycodestyle==2.8.0
- pycparser==2.21
- PyDispatcher==2.0.5
- pyflakes==2.4.0
- pyOpenSSL==22.0.0
- pyparsing==3.0.7
- pytest==6.2.5
- pytest-pythonpath==0.7.4
- queuelib==1.6.2
- Scrapy==2.5.1
- service-identity==21.1.0
- six==1.16.0
- toml==0.10.2
- Twisted==22.2.0
- typing_extensions==4.1.1
- w3lib==1.22.0
- zipp==3.7.0
- zope.interface==5.4.0
