import scrapy
from financial_webscraper_app.items import FinancialWebScraperItem

class FinancialSpider(scrapy.Spider):
    name = 'financial_spider'
    allowed_domains = ['google.com', 'markets.businessinsider.com', 'nasdaq.com', 'fool.com', 
                       'economist.com', 'marketwatch.com', 'ft.com', 'moneymorning.com', 
                       'thestreet.com', 'thisismoney.co.uk', 'kiplinger.com', 'investing.com', 
                       'wsj.com', 'forbes.com', 'reuters.com', 'bloomberg.com']
    start_urls = [
        'https://google.com/finance',
        'https://markets.businessinsider.com/index/nasdaq_100',
        'https://markets.businessinsider.com/index/s&p_500',
        'https://markets.businessinsider.com/',
        'https://markets.businessinsider.com/index/dow_jones',
        'https://www.nasdaq.com/market-activity/stocks/screener',
        'https://www.fool.com/',
        'https://www.economist.com/',
        'https://www.marketwatch.com/',
        'https://www.ft.com/world',
        'https://moneymorning.com/',
        'https://www.thestreet.com/',
        'https://www.thisismoney.co.uk/money/index.html',
        'https://www.kiplinger.com/',
        'https://www.investing.com/',
        'https://www.wsj.com/',
        'https://www.forbes.com/?sh=1877296a2254',
        'https://www.reuters.com/',
        'https://www.bloomberg.com/businessweek'
    ]

    def parse(self, response):
        item = FinancialWebScraperItem()
        item['headline'] = response.css('h1::text').get()
        item['article'] = response.css('p::text').getall()
        item['stock_price'] = response.css('.stock-price::text').get()
        item['graph'] = response.css('img::attr(src)').get()
        item['media'] = response.css('video::attr(src)').get()
        item['type'] = 'article'
        item['category'] = 'finance'
        item['keywords'] = response.css('meta[name=keywords]::attr(content)').get()
        yield item
