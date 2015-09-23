import numpy as np


class Cluster(object):

    def __init__(self, datapoints=None, is_noise=False):
        self._datapoints = [] if datapoints is None else datapoints
        self._is_noise = is_noise

    @property
    def datapoints(self):
        return self._datapoints

    @datapoints.setter
    def datapoints(self, value):
        self._datapoints = value

    @property
    def is_noise(self):
        return self._is_noise

    @is_noise.setter
    def is_noise(self, value):
        self._is_noise = value

    def __str__(self):
        if len(self.datapoints) > 0:
            return np.vstack(
                [d.data_vector for d in self.datapoints]
            ).__str__()
        else:
            return np.empty((0, 0), int).__str__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()