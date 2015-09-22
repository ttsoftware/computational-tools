from sklearn.metrics import jaccard_similarity_score
from week4.cluster import Cluster


class DBSCAN(object):
    def __init__(self, epsilon, min_size):
        self.epsilon = epsilon
        self.min_size = min_size

    def scan(self, dataset):
        """
        Dataset is a list of DataPoint's
        :rtype : object
        :param dataset:
        """
        noise_cluster = Cluster(is_noise=True)
        clusters = [noise_cluster]

        for datapoint in dataset:
            if datapoint.visited:
                continue

            datapoint.visited = True
            neighbour_points = self.region_query(dataset, datapoint)

            if len(neighbour_points) < self.min_size:
                datapoint.noise = True
                datapoint.belongs_to_cluster = True
                noise_cluster.datapoints += [datapoint]
            else:
                cluster = Cluster()
                self.expand_cluster(dataset, datapoint, neighbour_points, cluster)

                clusters += [cluster]

        return clusters

    def expand_cluster(self, dataset, datapoint, neighbour_points, cluster):
        """
        Expands cluster with epsilon-neighbouring datapoints not belonging to an existing cluster
        :param datapoint:
        :param neighbour_points:
        :param cluster:
        """
        cluster.datapoints += [datapoint]
        datapoint.belongs_to_cluster = True

        for new_datapoint in neighbour_points:

            if not new_datapoint.visited:

                new_datapoint.visited = True
                new_neighbour_points = self.region_query(dataset, new_datapoint)

                if len(new_neighbour_points) >= self.min_size:
                    neighbour_points += new_neighbour_points
                    neighbour_points = list(set(neighbour_points))

            if not new_datapoint.belongs_to_cluster:
                cluster.datapoints += [new_datapoint]
                new_datapoint.belongs_to_cluster = True

    def region_query(self, dataset, datapoint):
        """
        Returns a list of datapoints in datapoint's epsilon-neigbourhood
        :param datapoint:
        :return:
        """
        datapoints = []
        for new_datapoint in dataset:

            if new_datapoint != datapoint:

                score = 1 - jaccard_similarity_score(
                    datapoint.data_vector,
                    new_datapoint.data_vector
                )

                if score <= self.epsilon:
                    datapoints += [new_datapoint]

        return datapoints