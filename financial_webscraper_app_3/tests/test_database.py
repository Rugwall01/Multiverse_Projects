import unittest
from database.db_utils import fetch_data

class TestDatabase(unittest.TestCase):
    def test_fetch_data(self):
        query = {}
        data = fetch_data(query)
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
