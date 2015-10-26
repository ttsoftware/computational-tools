from pprint import pprint
from pymongo import MongoClient


class Mongodb(object):
    def __init__(self, dbname):

        self.client = MongoClient()
        self.db = self.client[dbname]

    def group_by(self, obj, key, condition, reduce_function, initial):

        documents = []
        for doc in self.db[obj].group(key=key, condition=condition, reduce=reduce_function, initial=initial):
            documents += [doc]

        return documents

    def find_all(self, obj):

        documents = []
        for doc in self.db[obj].find():
            documents += [doc]

        return documents

    def find_by(self, obj, selector):

        documents = []
        for doc in self.db[obj].find(selector):
            documents += [doc]

        return documents

    def join(self, collection1, obj, fk1, fk2):
        return filter(
            lambda x: True if x[fk1] == obj[fk2] else False,
            collection1
        )

    def join_in(self, collection1, collection2, fk):
        return filter(
            lambda x: True if x[fk] in collection2 else False,
            collection1
        )
