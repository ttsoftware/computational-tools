from mrjob.job import MRJob
from mrjob.step import MRStep


class exercise_3(MRJob):

    def steps(self):
        return [
            MRStep(
                mapper=self.mapper,
                reducer=self.friend_pairs
            ),
            MRStep(
                reducer=self.friend_intersection
            )
        ]

    def mapper(self, _, line):
        user, friend = line.split()
        yield int(user), int(friend)
        yield int(friend), int(user)  # make sure we have the opposite relation from B to A

    def friend_pairs(self, user, friends):
        friend_list = reduce(lambda x, y: x + [y], friends, [])

        for friend in friend_list:
            yield sorted([user, friend]), friend_list

    def friend_intersection(self, friend_pair, combined_friends):

        combined_friends = reduce(lambda x, y: x + [y], combined_friends, [])
        intersection = []

        for friend in combined_friends[0]:
            if friend in combined_friends[1]:
                intersection += [friend]

        yield friend_pair, intersection
