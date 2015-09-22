import pickle
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

        print matrix

        return map(lambda x: DataPoint(x), matrix)