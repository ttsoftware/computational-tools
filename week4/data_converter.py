import pickle
import numpy as np
from scipy.sparse import csr_matrix
from datapoint import DataPoint


class DataConverter(object):

    @staticmethod
    def convert(filename):
        """
        Converts file to a list of data points
        :param filename:
        :return:
        """
        pkl_file = open(filename, 'rb')
        data = pickle.load(pkl_file)
        matrix = csr_matrix(data).todense()

        return map(lambda (i, x): DataPoint(x, i), enumerate(matrix))