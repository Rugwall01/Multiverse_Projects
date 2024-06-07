import scrapy

class FinancialWebScraperItem(scrapy.Item):
    headline = scrapy.Field()
    article = scrapy.Field()
    stock_price = scrapy.Field()
    graph = scrapy.Field()
    media = scrapy.Field()
    type = scrapy.Field()
    category = scrapy.Field()
    keywords = scrapy.Field()
