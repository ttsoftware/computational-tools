import hashlib
import numpy
from scipy.spatial.distance import jaccard
from week4.cluster import Cluster


class DBSCAN(object):

    def __init__(self, epsilon, min_size):
        self.epsilon = epsilon
        self.min_size = min_size
        self.regions = {}

    def scan(self, dataset):
        """
        Dataset is a list of DataPoint's
        :rtype : object
        :param dataset:
        """
        clusters = []

        for datapoint in dataset:
            if str(datapoint.data_vector) not in self.regions:
                self.regions[str(datapoint.data_vector)] = self.region_query(dataset, datapoint)

        for datapoint in dataset:
            if datapoint.visited:
                continue

            datapoint.visited = True
            neighbour_points = self.regions[str(datapoint.data_vector)]

            if len(neighbour_points) < self.min_size:
                datapoint.is_noise = True
            else:
                cluster = Cluster()
                self.expand_cluster(dataset, datapoint, neighbour_points, cluster)
                clusters.append(cluster)

        noise_cluster = Cluster(is_noise=True)
        for datapoint in dataset:
            if datapoint.is_noise:
                noise_cluster.datapoints.append(datapoint)

        clusters.append(noise_cluster)
        return clusters

    def expand_cluster(self, dataset, datapoint, neighbour_points, cluster):
        """
        Expands cluster with epsilon-neighbouring datapoints not belonging to an existing cluster
        :param datapoint:
        :param neighbour_points:
        :param cluster:
        """
        cluster.datapoints.append(datapoint)
        datapoint.belongs_to_cluster = True

        for new_datapoint in neighbour_points:

            if not new_datapoint.visited:

                new_datapoint.visited = True
                new_neighbour_points = self.regions[str(new_datapoint.data_vector)]

                if len(new_neighbour_points) >= self.min_size:
                    neighbour_points += new_neighbour_points

            if not new_datapoint.belongs_to_cluster:
                cluster.datapoints.append(new_datapoint)
                new_datapoint.is_noise = False
                new_datapoint.belongs_to_cluster = True

    def region_query(self, dataset, datapoint):
        """
        Returns a list of new datapoints in datapoint's epsilon-neigbourhood
        :param datapoint:
        :return:
        """
        datapoints = [datapoint]

        for new_datapoint in dataset:

            if new_datapoint != datapoint:

                distance = jaccard(
                    datapoint.data_vector,
                    new_datapoint.data_vector
                )

                if distance <= self.epsilon:
                    datapoints.append(new_datapoint)

        return datapoints