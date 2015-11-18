from mrjob.job import MRJob
from mrjob.step import MRStep


class exercise_2(MRJob):

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                reducer=self.reducer
            ),
            MRStep(
                reducer=self.combine_reduced_values
            )
        ]

    def mapper(self, _, line):
        for word in line.split():
            yield word, 1

    def reducer(self, key, values):
        yield None, sum(values) % 2 == 0

    def combine_reduced_values(self, _, values):
        yield "Does an Euler tour exist?", self.is_list_true(values)

    @staticmethod
    def is_list_true(l):
        is_true = True
        for x in l:
            is_true = is_true and x
        return is_true
