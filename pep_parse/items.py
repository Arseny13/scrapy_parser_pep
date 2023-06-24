import scrapy


class PepParseItem(scrapy.Item):
    """Класс item для pep."""
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
