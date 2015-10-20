from collections import deque
import pickle
import time
import sys

class Point():
    def __init__(self, features, row_number):
        self.cluster = None
        self.visited = False
        self.features = features
        self.multiplicity = 1
        # Add a list that keeps track of which row these points had in the original SciPy array (zero-indexed):
        self.org_row_numbers = [row_number]

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '10':
        # Testdata 10x10
        testrun(size=10, eps=0.4, MinPts=2)
    elif sys.argv[1] == '100':
        # Testdata 100x100
        testrun(size=100, eps=0.3, MinPts=2)
    elif sys.argv[1] == '1000':
        # Testdata 1000x1000
        testrun(size=1000, eps=0.15, MinPts=2)
    elif sys.argv[1] == '10000':
        # Testdata 10000x10000
        testrun(size=10000, eps=0.15, MinPts=2)
    elif sys.argv[1] == '100000':
        # Testdata 100000x100000
        testrun(size=100000, eps=0.15, MinPts=2)
    else:
        print('Error in input argument')
        sys.exit()

def sparse_to_python(sparse_mat):
    # Convert the Scipy sparse matrix to a pure native Python structure, using my Point class.
    # And remove duplicate points, instead storing a multiplicity with the remaining point.
    multiplicityDict = {}
    D = []
    for row_number, row in enumerate(sparse_mat):
        indices = tuple(row.indices)
        if indices in multiplicityDict:
            point = multiplicityDict[indices]
            point.multiplicity += 1
            point.org_row_numbers.append(row_number)
        else:
            point = Point(set(indices), row_number)
            D.append(point)
            multiplicityDict[indices] = point
    return D

def similarities(D):
    # Make a dict where each key is a feature, and the value being stored is a list of the points that have this feature.
    similarityDict = {}
    for point in D:
        for feature in point.features:
            if feature in similarityDict:
                similarityDict[feature].append(point)
            else:
                similarityDict[feature] = [point]
    return similarityDict

def neighborUnpack(neighbors):
    # Returns the actual number of neigbors in 'neigbors' by looking at multiplicity
    return sum(n.multiplicity for n in neighbors)

def DBSCAN(D, eps, MinPts, similarityDict):
    C = 1
    for P in D:
        if P.visited:
            continue
        P.visited = True
        NeighborPts = regionQuery(D, P, eps, similarityDict)
        if neighborUnpack(NeighborPts) >= MinPts:
            # Make a new cluster
            expandCluster(D, P, NeighborPts, C, eps, MinPts, similarityDict)
            C += 1
    # return number of clusters found including None class (noise class)
    return C

def expandCluster(D, P, NeighborPts, C, eps, MinPts, similarityDict):
    queue = deque(NeighborPts)
    P.cluster = C
    while queue:
        P2 = queue.popleft()
        if not P2.visited:
            P2.visited = True
            NeighborPts2 = regionQuery(D, P2, eps, similarityDict)
            if neighborUnpack(NeighborPts2) >= MinPts:
                queue.extend(NeighborPts2)
        if P2.cluster == None:
            P2.cluster = C

def jaccardDistance(p1, p2):
    intersection = len(p1.features.intersection(p2.features))
    jDis = 1 - intersection / ( len(p1.features) + len(p2.features) - intersection)
    return jDis

def regionQuery(D, P, eps, similarityDict):
    # return all points within P's eps-neighborhood (including P)
    neighbors = []
    potential_neighbors = set()
    for feature in P.features:
        for point in similarityDict[feature]:
            potential_neighbors.add(point)
    for point in potential_neighbors:
        jDis = jaccardDistance(P, point)
        if jDis <= eps:
            neighbors.append(point)
    return neighbors

def getTestdata(s_point_count):
    s_point_count = str(s_point_count)
    data = pickle.load(open('test_files/data_%spoints_%sdims.dat' % (s_point_count, s_point_count), 'rb'), encoding='latin1')
    return data

def largestCluster(D):
    # Return the number of elements in the largest cluster
    clusters = {}
    for point in D:
        if point.cluster in clusters:
            clusters[point.cluster] += point.multiplicity
        else:
            clusters[point.cluster] = point.multiplicity
    # Remove the None class (noise class)
    clusters.pop(None, None)
    largest_cluster = max(clusters, key = lambda x: clusters[x])
    nElements = clusters[largest_cluster]
    return nElements

def testrun(size=None, eps=None, MinPts=None):
    print('Size', size, 'x', size, '\n')

    t0 = time.time()
    D = getTestdata(size)
    t1 = time.time()
    tot = t1 - t0
    print('Load data using Pickle in:      ', round(t1-t0, 2), 'seconds')

    t0 = time.time()
    D = sparse_to_python(D)
    similarityDict = similarities(D)
    t1 = time.time()
    tot += t1 - t0
    print('Prepare data structure in:      ', round(t1-t0, 2), 'seconds')

    t0 = time.time()
    C = DBSCAN(D, eps, MinPts, similarityDict)
    t1 = time.time()
    tot += t1 - t0
    print('Running DBSCAN in:              ', round(t1-t0, 2), 'seconds')
    print('Total running time:             ', round(tot, 2), 'seconds')

    print('\nClasses incl noise class:       ', C,)
    print('Unique points:                  ', len(D), 'out of', size)
    nElements = largestCluster(D)
    print('Elements in the largest cluster:', nElements)

if __name__ == '__main__':
    main()
