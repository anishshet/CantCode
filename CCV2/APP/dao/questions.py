from utils.mongodb_fun import get_mongodb_collection
import bson

def get_list_of_questions():
    question_collection = get_mongodb_collection("question")
    return list(question_collection.find())

def get_question_by_id(id):
    question_collection = get_mongodb_collection("question")
    return question_collection.find_one({"_id": bson.objectid.ObjectId(id)})