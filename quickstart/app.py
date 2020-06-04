from flask import Flask, request
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api()
api.init_app(app)

# A Minimal API
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# Resourceful Routing
todos = {}

@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


@api.route('/todo1')
class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world'}


@api.route('/todo2')
class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world'}, 201


@api.route('/todo3')
class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}
