from flask import request
from flask_restful import Resource
from dao.user import validate_user


class Login(Resource):
    def post(self):
        request_data = request.get_json(force=True)
        return validate_user(request_data["user_name"], request_data["password"])
