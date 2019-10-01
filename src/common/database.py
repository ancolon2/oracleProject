import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['oracle']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        data = Database.DATABASE[collection].find(query)
        return data

    @staticmethod
    def find_one(collection, query):
        data = Database.DATABASE[collection].find_one(query)
        return data
