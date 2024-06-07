from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.financial_data

class FinancialData:
    def __init__(self, headline, article, stock_price, graph, media, type, category, keywords):
        self.headline = headline
        self.article = article
        self.stock_price = stock_price
        self.graph = graph
        self.media = media
        self.type = type
        self.category = category
        self.keywords = keywords

    def save(self):
        db.financial_data.update_one(
            {'headline': self.headline},
            {'$set': self.__dict__},
            upsert=True
        )
