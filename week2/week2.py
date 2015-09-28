import re


def read_matrix(filename):
    """
    Reads a file and tries to construct a matrix from data in the file

    :param filename: name of file it be read
    :return: list of lists of the numbers in the file
    """
    f = open(filename, 'r')

    # Reads all lines from file into list
    lines = f.readlines()

    matrix_list = []
    for line in lines:
        # Using list comprehension to construct a new list of the numbers contained in each line
        matrix_list.append([float(c) for c in re.split("[, ]", line.rstrip())])
    f.close()
    return matrix_list


def write_matrix(array, filename):
    """
    Interprets a matrix (list of lists) and writes it to filename

    :param array: Matrix (list of lists) to be written to file
    :param filename: Name of the file to write to
    """
    f = open(filename, 'w')
    output = ""
    for l in array:
        for c in l:
            output += str(c) + ' '
        output = output[:-1] + '\n'
    f.write(output)
    f.close()


def bit_strings(N):
    """
    Takes a number N and constructs all bit permutations of size N

    :param N: Size of permutations
    :return: List of all permutations of bit strings of size N
    """
    pools = [[0, 1]] * N
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    return result


def bag_of_words(filename):
    """
    Reads a very specific json file and constructs a bag-of-words representation
    of people's comments and their ability to get free pizza.

    :param filename: Name of file to be read
    :return: Bag-of-words representation
    """
    f = open(filename)
    lines = f.readlines()
    request_texts = []
    theD = {}
    cnt = 0

    # Regular expression that matches request_text line
    pat = re.compile('\s+"request_text": "(?P<text>.+)"')
    # Regular expression that matches requester_received_pizza line
    patr = re.compile('\s+"requester_received_pizza": (?P<pizza>.+),')
    results = []
    for line in lines:
        # If line is matches request_text
        result = re.search(pat, line)
        if result:
            # Saves the request_text for later use
            request_texts.append(result.group('text').lower())

            # Iterate over all words
            for word in re.findall("[\w\']+", result.group('text')):
                word = word.lower()

                # Put words not already found into dictionary
                if word not in theD.keys():
                    theD[word] = cnt
                    cnt += 1

        # Make list of all the results of pizze beggars.
        pizza_result = re.search(patr, line)
        if pizza_result:
            results.append(0) if pizza_result.group('pizza') == 'false' else results.append(1)

    # Use word dictionary to create bag-of-words
    bag = []
    for i, text in enumerate(request_texts):
        vec = [0] * len(theD) + [results[i]]
        for word in re.findall("[\w\']+", text):
            vec[theD[word]] += 1
        bag.append(vec)

    return bag


if "__main__" == __name__:
    # print read_matrix('matrix')
    # write_matrix([[2, 3, 5], [1, 4, 2]], 'matrix2')
    print bit_strings(3)
    # print bag_of_words("pizza-train.json")
