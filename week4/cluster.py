import numpy as np


class Cluster(object):

    def __init__(self, datapoints=[], is_noise=False):
        self._datapoints = datapoints
        self.is_noise = is_noise

    @property
    def datapoints(self):
        return self._datapoints

    @datapoints.setter
    def datapoints(self, value):
        self._datapoints = value

    def __str__(self):
        if len(self.datapoints) > 0:
            return np.vstack(
                [d.data_vector for d in self.datapoints]
            ).__str__()
        else:
            return np.empty((0, 0), int).__str__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()