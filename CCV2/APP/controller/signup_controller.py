from flask import request
from flask_restful import Resource
from dao.user import create_user, update_user, get_user


class Signup(Resource):
    def get(self, id):
        response = get_user(id)
        # print(get_user(id))
        return {'user': response}

    def post(self):
        request_data = request.get_json(force=True)
        return create_user(request_data)

    def put(self, id):
        request_data = request.get_json(force=True)
        return update_user(id, request_data)
