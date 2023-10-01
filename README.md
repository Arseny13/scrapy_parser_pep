# scrapy_parser_pep

<h4>Автор:</h4>

**Изимов Арсений**  - студент Яндекс.Практикума Когорта 17+
https://github.com/Arseny13

<h2>Техническое описание проекта</h2>

-   спарсить данные обо всех документах PEP;
-   сравнить статус на странице PEP со статусом в общем списке;
-   посчитать количество PEP в каждом статусе и общее количество PEP; данные о статусе документа нужно брать со страницы каждого PEP, а не из общей таблицы;
-   сохранить результат в табличном виде в csv-файл.

Парсер должен выводить собранную информацию в два файла .csv:

-   В первый файл нужно вывести список всех PEP: номер, название и статус
-   Второй файл должен содержать сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). В последней строке этого файла в колонке «Статус» должно стоять слово Total, а в колонке «Количество» — общее количество всех документов.


<h2>Как использовать</h2>

Активировать виртуальное окружение: `python -m venv venv`

Установить зависимости из requirements.txt : `pip install - r requirements.txt`

Запустить паука: `scrapy crawl pep`

Результат работы появится в папке `results` в формате 2х csv файлов.

<h2>Используемые технологии</h2>
- Scrapy==2.5.1
