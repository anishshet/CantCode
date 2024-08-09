from dao.questions import get_list_of_questions, get_question_by_id
from flask import request
from flask_restful import Resource
from dao.user import validate_user


class Question(Resource):
    def get(self,id=None):
        if id: 
            y =  get_question_by_id(id)
            y["_id"] = str(y["_id"])
            return y
        x = get_list_of_questions()
        for i in range(len(x)):
            x[i]["_id"] = str(x[i]["_id"])
        return x