BOT_NAME = 'financial_webscraper_app'

SPIDER_MODULES = ['financial_webscraper_app.spiders']
NEWSPIDER_MODULE = 'financial_webscraper_app.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'financial_webscraper_app.pipelines.MongoDBPipeline': 300,
}

MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'financial_data'
