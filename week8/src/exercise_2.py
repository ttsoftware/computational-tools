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
                reducer=self.combine
            )
        ]

    def mapper(self, _, line):
        for word in line.split():
            yield word, 1

    def reducer(self, key, values):
        yield None, sum(values) % 2 == 0

    def combine(self, _, values):
        yield None, self.is_list_true(values)

    def is_list_true(self, l):
        is_true = True
        for x in l:
            is_true = is_true and x
        return is_true
