from __future__ import division
import json
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.feature_extraction import FeatureHasher


directory = "../../full/"


def bag_of_words(lines):

    uniq = set()

    for line in lines:
        # Iterate over all words
        for word in line[0].split():

            # Put words not already found into dictionary
            uniq.add(word)

    uniq_dict = {}
    for j, word in enumerate(uniq):
        uniq_dict[word] = j

    uniq_len = len(uniq)

    # Use word dictionary to create bag-of-words
    bag = []
    for line in lines:
        vec = [0] * uniq_len
        for word in line[0].split():
            vec[uniq_dict[word]] += 1
        bag.append((vec, (1 if 'earn' in line[1] else 0)))

    return bag


if __name__ == "__main__":
    articles = []
    for i in range(21):
        f = open(directory + "reuters-0" + (str(i) if i >= 10 else "0" + str(i)) + ".json", 'r')
        articles += json.loads(f.read())
        f.close()

    articles = reduce(lambda x, y: x + ([y] if ('topics' in y.keys())
                                               and ('body' in y.keys())
                                               and (len(y['topics']) > 0)
                                               and (len(y['body']) > 0)
                                            else []), articles, [])

    lines = map(lambda x: (x['body'].lower(), x['topics']), articles)

    bow = bag_of_words(lines)
    print "Amount of lines: " + str(len(bow))
    print "Amount of words: " + str(len(bow[0][0]))

    # training_set = bow[:int(round(len(bow)*0.8))]
    # training_set_data = [row[0] for row in training_set]
    # training_set_target = [row[1] for row in training_set]
    #
    # test_set = bow[-int(round(len(bow)*0.2)):]
    # test_set_data = [row[0] for row in test_set]
    # test_set_target = [row[1] for row in test_set]
    #
    # classifier = rfc()
    # classifier.fit(training_set_data, training_set_target)
    # predictions = classifier.predict(test_set_data)
    #
    # accuracy = []
    # for i, prediction in enumerate(predictions):
    #     accuracy += [test_set_target[i] == prediction]
    # accuracy = accuracy.count(True) / len(test_set_target)
    #
    # print "Accuracy of classifier: " + str(accuracy) + "%"

    hasher = FeatureHasher()
    hashed_bow = hasher.transform([row[0] for row in bow])

    print hashed_bow
