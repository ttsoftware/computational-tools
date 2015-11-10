from mrjob.job import MRJob

class exercise_2(MRJob):

    def mapper(self, _, line):
        for word in line.split():
            yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)

    def combiner(self, key, values):
