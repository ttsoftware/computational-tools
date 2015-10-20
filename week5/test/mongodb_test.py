from pprint import pprint
import unittest
from week5.mongodb import Mongodb


class MongodbCase(unittest.TestCase):

    def test_find_all(self):

        db = Mongodb('Northwind')
        pprint(db.find_all('customers'))

    def test_find_by(self):

        db = Mongodb('Northwind')
        pprint(db.find_by('customers', {'City': 'Berlin'}))

if __name__ == '__main__':
    unittest.main()
