
class Cluster(object):

    def __init__(self, datapoints=[], is_noise=False):
        self.datapoints = datapoints
        self.is_noise = is_noise