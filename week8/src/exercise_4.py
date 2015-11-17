from mrjob.job import MRJob
from mrjob.step import MRStep


class exercise_3(MRJob):
    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                reducer=self.reducer
            )
        ]

    def mapper(self, _, line):
        yield line.split()

    def reducer(self, key, value):
        yield key, value
