from mrjob.job import MRJob
from mrjob.protocol import JSONProtocol


class exercise_1(MRJob):

    def mapper(self, _, line):
        for word in line.split():
            yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)