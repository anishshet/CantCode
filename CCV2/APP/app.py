from controller.solution import Solution
from controller.questions_controller import Question
from flask import Flask, render_template
from flask_restful import Resource, Api
from controller.login_controller import Login

from controller.signup_controller import Signup
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(Signup, '/signup', '/signup/<string:id>')
api.add_resource(Login, '/login')
api.add_resource(Question, '/question', '/question/<string:id>')
api.add_resource(Solution, '/solution')


if __name__ == '__main__':
    app.run(debug=True, port=5678)
