
class DataPoint(object):

    def __init__(self, data_vector, index):
        """
        data_vector is a numpy matrix
        index should be the unique index in the original matrix
        :param data_vector:
        """
        self.data_vector = data_vector
        self._index = index
        self._visited = False
        self._belongs_to_cluster = False
        self._noise = False

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, value):
        self._visited = value

    @property
    def belongs_to_cluster(self):
        return self._belongs_to_cluster

    @belongs_to_cluster.setter
    def belongs_to_cluster(self, value):
        self._belongs_to_cluster = value

    @property
    def is_noise(self):
        return self._noise

    @is_noise.setter
    def is_noise(self, value):
        self._noise = value

    def __str__(self): 
        return str(self.index) + ":" + self.data_vector.__str__()

    def __eq__(self, other):
        return self.index == other.index