from mrjob.job import MRJob
from mrjob.step import MRStep


class exercise_3(MRJob):

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper_one,
            ),
            MRStep(
                mapper=self.friends_of_friends,
                reducer=self.test_reducer
            )
        ]

    def mapper_one(self, _, line):
        user, friend = line.split()
        yield user, friend

    def friends_of_friends(self, user, friends):
        for friend in friends:
            yield [user, friend].sort(), friends

    def test_reducer(self, key, values):
        print key, reduce(lambda x, y: x + [y], values, [])
        yield key, values
