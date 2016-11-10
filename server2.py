from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


todos={}
class TodoSimple(Resource):

    def __init__(self):
        todos={}

    def get(self, todo_id):
        if todo_id in todos:
           return {todo_id: todos[todo_id]}
        else:
           return {todo_id:'Not Found'}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        if todo_id in todos:
           del todos[todo_id]
           return {todo_id:'Deleted'}
        else:
           return {todo_id:'Not Found'}


api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
