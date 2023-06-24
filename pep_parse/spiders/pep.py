import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Класс паука для pep."""
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Функция парса pep."""
        all_peps = response.css('a[href^="pep-"]')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Функция парса для отдельного pep."""
        title = response.css('h1.page-title::text').get().split(' – ')
        number, name = int(title[0].split(' ')[1]), title[1]
        data = {
            'number': number,
            'name': name,
            'status': response.css('dt:contains("Status") + dd ::text').get(),
        }
        yield PepParseItem(data)
