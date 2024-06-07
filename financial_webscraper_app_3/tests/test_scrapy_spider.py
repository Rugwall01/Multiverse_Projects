import unittest
from scrapy_spider.spiders.financial_spider import FinancialSpider

class TestFinancialSpider(unittest.TestCase):
    def setUp(self):
        self.spider = FinancialSpider()

    def test_parse(self):
        # Add test logic
        pass

if __name__ == '__main__':
    unittest.main()
