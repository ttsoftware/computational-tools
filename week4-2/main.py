import pickle
from scipy.sparse import csr_matrix
from sklearn.metrics import jaccard_similarity_score


def scan(filename, epsilon, min_size):

    pkl_file = open(filename, 'rb')
    data = pickle.load(pkl_file)
    dataset = [{
        "data": x,
        "visited": False,
        "in_cluster": False,
        "is_noise": False
    } for x in csr_matrix(data).todense()]

    clusters = []

    for datapoint in dataset:
        if datapoint['visited']:
            continue

        datapoint['visited'] = True
        neighbour_points = region_query(dataset, datapoint, epsilon)

        if len(neighbour_points) < min_size:
            datapoint['is_noise'] = True
        else:
            cluster = expand_cluster(dataset, datapoint, neighbour_points, epsilon, min_size)
            clusters.append(cluster)

    noise_cluster = {'datapoints': [], 'is_noise': True}
    for datapoint in dataset:
        if datapoint['is_noise']:
            noise_cluster['datapoints'].append(datapoint)

    clusters.append(noise_cluster)
    return clusters


def expand_cluster(dataset, datapoint, neighbour_points, epsilon, min_size):
    """
    Expands cluster with epsilon-neighbouring datapoints not belonging to an existing cluster
    :param datapoint:
    :param neighbour_points:
    :param cluster:
    """
    cluster = {'datapoints': [datapoint], 'is_noise': False}
    datapoint['in_cluster'] = True

    for new_datapoint in neighbour_points:

        if not new_datapoint['visited']:

            new_datapoint['visited'] = True
            new_neighbour_points = region_query(dataset, new_datapoint, epsilon)

            if len(new_neighbour_points) >= min_size:
                neighbour_points += new_neighbour_points

        if not new_datapoint['in_cluster']:
            cluster['datapoints'].append(new_datapoint)
            new_datapoint['is_noise'] = False
            new_datapoint['in_cluster'] = True

    return cluster


def region_query(dataset, datapoint, epsilon):
    """
    Returns a list of new datapoints in datapoint's epsilon-neigbourhood
    :param datapoint:
    :return:
    """
    datapoints = [datapoint]

    dataset.remove(datapoint)
    for new_datapoint in dataset:

        distance = 1 - jaccard_similarity_score(
            datapoint['data'],
            new_datapoint['data']
        )

        if distance <= epsilon:
            datapoints.append(new_datapoint)

    return datapoints

if "__main__" == __name__:
    print len(scan("/home/rasmus/Documents/computational tools for big data/computational-tools/week4/test_files/data_1000points_1000dims.dat", 0.15, 2))