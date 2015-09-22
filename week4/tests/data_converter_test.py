import os
import unittest
from week4.data_converter import DataConverter


class DataConverterTest(unittest.TestCase):

    def test_convert(self):
        filename = os.path.dirname(__file__) + '/../test_files/data_10points_10dims.dat'

        dataset = DataConverter.convert(filename)

        print dataset[0].data_vector
        print dataset[1].data_vector
        print dataset[2].data_vector

        #self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()