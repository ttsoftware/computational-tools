
class DataPoint(object):

    def __init__(self, data_vector):
        """
        data_vector is a numpy matrix
        :param data_vector:
        """
        self.data_vector = data_vector
        self.visited = False
        self.belongs_to_cluster = False
        self.noise = None