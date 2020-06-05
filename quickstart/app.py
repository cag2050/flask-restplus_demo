import os
import click

from flask import Flask, request, send_from_directory
from flask_restplus import Api, Resource, reqparse, fields

app = Flask(__name__)
api = Api()
api.init_app(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='images/favicon.ico')

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


# Endpoints
api.add_resource(HelloWorld, '/world')


# Argument Parsing
@api.route('/todos')
class Todos(Resource):
    requestParser = reqparse.RequestParser()
    requestParser.add_argument('rate', type=int, help='Rate to charge for this resource')

    @api.expect(requestParser)
    def post(self):
        args = self.requestParser.parse_args()
        # 验证通过，才会打印
        click.echo(args)
        return {'test': 'reqparse'}


# Data Formatting
model = api.model('Model', {
    'task': fields.String,
    'uri': fields.Url('need_do')
})


class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'


@api.route('/need_do')
class NeedDo(Resource):
    @api.marshal_with(model)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')
