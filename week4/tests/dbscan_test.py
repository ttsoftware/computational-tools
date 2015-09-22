import os
import unittest
from week4.data_converter import DataConverter
from week4.dbscan import DBSCAN


class DBSCANTest(unittest.TestCase):

    def test_scan(self):
        filename = os.path.dirname(__file__) + '/../test_files/data_10points_10dims.dat'
        dataset = DataConverter.convert(filename)

        epsilon = 0.4
        min_size = 2
        dbscan = DBSCAN(epsilon, min_size)
        clusters = dbscan.scan(dataset)

        print len(clusters)
        print clusters[0] == clusters[1] == clusters[2]
        print clusters[0]
        print clusters[1]
        print clusters[2]

if __name__ == '__main__':
    unittest.main()