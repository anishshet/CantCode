from pymongo import MongoClient


def get_mongodb_collection(collection_name):
    mongo_client = MongoClient("mongodb://127.0.0.1:27017/")
    db = mongo_client["cant_code"]
    # print(db[collection_name])
    return db[collection_name]
