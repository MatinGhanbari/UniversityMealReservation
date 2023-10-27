from pymongo import MongoClient


class BaseRepository:
    def __init__(self, collection_name):
        self.client = MongoClient()
        self.db = self.client['my_database']
        self.collection = self.db[collection_name]

    def find_one(self, id):
        document = self.collection.find_one({'_id': id})
        return document

    def insert_one(self, document):
        self.collection.insert_one(document)

    def delete_one(self, id):
        self.collection.delete_one({'_id': id})
