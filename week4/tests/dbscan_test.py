import os
import unittest
from sklearn.metrics.metrics import jaccard_similarity_score
from week4.data_converter import DataConverter
from week4.dbscan import DBSCAN


class DBSCANTest(unittest.TestCase):

    def test_scan_10(self):
        filename = os.path.dirname(__file__) + '/../test_files/data_10points_10dims.dat'
        dataset = DataConverter.convert(filename)

        epsilon = 0.4
        min_size = 2
        dbscan = DBSCAN(epsilon, min_size)
        clusters = dbscan.scan(dataset)

        self.assertEqual(4, len(clusters))

    def test_scan_100(self):
        filename = os.path.dirname(__file__) + '/../test_files/data_100points_100dims.dat'
        dataset = DataConverter.convert(filename)

        epsilon = 0.3
        min_size = 2
        dbscan = DBSCAN(epsilon, min_size)
        clusters = dbscan.scan(dataset)

        self.assertEqual(6, len(clusters))

    def test_scan_1000(self):
        filename = os.path.dirname(__file__) + '/../test_files/data_1000points_1000dims.dat'
        dataset = DataConverter.convert(filename)

        epsilon = 0.15
        min_size = 2
        dbscan = DBSCAN(epsilon, min_size)
        clusters = dbscan.scan(dataset)

        self.assertEqual(9, len(clusters))

    def test_scan_10000(self):
        filename = os.path.dirname(__file__) + '/../test_files/data_10000points_10000dims.dat'
        dataset = DataConverter.convert(filename)

        epsilon = 0.15
        min_size = 2
        dbscan = DBSCAN(epsilon, min_size)
        clusters = dbscan.scan(dataset)

        self.assertEqual(394, len(clusters))

    def test_scan_100000(self):
        filename = os.path.dirname(__file__) + '/../test_files/data_100000points_100000dims.dat'
        dataset = DataConverter.convert(filename)

        epsilon = 0.15
        min_size = 2
        dbscan = DBSCAN(epsilon, min_size)
        clusters = dbscan.scan(dataset)

        self.assertEqual(1692, len(clusters))

if __name__ == '__main__':
    unittest.main()