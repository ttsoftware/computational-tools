import os
from pprint import pprint
import unittest
from week5.sqlite import SQLite


class SQLiteTest(unittest.TestCase):

    def test_get_table_names(self):

        db = SQLite(os.path.dirname(__file__) + '/../data/northwind.db')

        tables = db.get_table_names()

        pprint(tables)

    def test_find_all(self):

        db = SQLite(os.path.dirname(__file__) + '/../data/northwind.db')
        data = db.find_all('Customers')

        pprint(data)

    def test_find_by(self):

        db = SQLite(os.path.dirname(__file__) + '/../data/northwind.db')
        data = db.find_by('Customers', 'City', 'Berlin')

        pprint(data)

if __name__ == '__main__':
    unittest.main()
