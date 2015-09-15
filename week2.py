import itertools, json


def read_matrix(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    matrix_list = []
    for line in lines:
        matrix_list.append([c for c in line.rstrip().split(' ')])
    f.close()
    return matrix_list


def write_matrix(array, filename):
    f = open(filename, 'w')
    output = ""
    for l in array:
        for c in l:
            output += str(c) + ' '
        output = output[:-1] + '\n'
    f.write(output)
    f.close()


def bit_strings(N):
    return list(itertools.product(range(2), repeat=N))


def bag_of_words(filename):
    f = open(filename)
    j = json.load(f)
    theD = {}
    for dic in j:
        for word in dic['request_text'].rstrip().split(' '):
            if word in theD.keys():
                theD[word] += 1
            else:
                theD[word] = 1
    return theD


if "__main__" == __name__:
    #print read_matrix('matrix')
    #write_matrix([[2, 3], [1, 4]], 'matrix2')
    #print bit_strings(3)
    print bag_of_words("pizza-train.json")