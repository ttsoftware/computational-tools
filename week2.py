import re



def read_matrix(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    matrix_list = []
    for line in lines:
        matrix_list.append([float(c) for c in re.split("[, ]", line.rstrip())])
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
    pools = [[0, 1]] * N
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    return result


def bag_of_words(filename, limit = None):
    f = open(filename)
    lines = f.readlines()
    request_texts = []
    theD = {}
    cnt = 0
    pat = re.compile('\s+"request_text": "(?P<text>.+)"')
    patr = re.compile('\s+"requester_received_pizza": (?P<pizza>.+),')
    results = []
    for line in lines:
        result = re.search(pat, line)
        if result:
            request_texts.append(result.group('text').lower())
            for word in re.findall("[\w\']+", result.group('text')):
                word = word.lower()
                if word not in theD.keys():
                    theD[word] = cnt
                    cnt += 1
        pizza_result = re.search(patr, line)
        if pizza_result:
            results.append(0) if pizza_result.group('pizza') == 'false' else results.append(1)
            if limit and len(results) == limit:
                break

    bag = []
    for i, text in enumerate(request_texts):
        vec = [0] * len(theD) + [results[i]]
        for word in re.findall("[\w\']+", text):
            vec[theD[word]] += 1
        bag.append(vec)

    return bag


if "__main__" == __name__:
    # print read_matrix('matrix')
    # write_matrix([[2, 3], [1, 4]], 'matrix2')
    # print bit_strings(3)
    print bag_of_words("pizza-train.json")
