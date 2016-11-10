from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

app = Flask(__name__)
api = Api(app)

todos={}
e = create_engine('sqlite:///index.db')

class TodoSimple(Resource):

    def __init__(self):
        todos={}

    def get(self, word):
        if word in todos:
           return {word: todos[word]}
        else:
           return {word:'Not Found'}

    def put(self, word,doc):
        w= request.form['word']
        d= request.form['doc']
        print(str.format("method Word is <{}>\nDoc  is <{}>",word,doc))
        print(str.format("form   Word is <{}>\nDoc  is <{}>",w,d))
        conn = e.connect()
        cur=conn.execute("select word,file from Document where word='%s'"%word)
        result=cur.fetchall()
        if len(result)==0:
            query = conn.execute("insert into Document (word,file)  values ('%s','%s')"%(word,doc))
            return {word: str.format("<{}> added to doc <{}>",word,doc)}
        else:
            #Need to check if doc is already stored for word
            #Data is returned as a list of tuples
            if doc in result[0][0].split():
               return {word: str.format("<{}> already listed in <{}>",word,doc)}
            else:
                doc=result[0][0]+' '+doc
                conn.execute("update Document set file='%s' where word='%s'"%(doc,word))
                return {word: str.format("<{}> added to doc <{}>",word,doc)}

    def delete(self, word):
        #if word in todos:
        #   del todos[word]
        #    return {word:'Deleted'}
        #else:
           return {word:'Not Found'}

class Index(Resource):
    def get(self,word):
        conn = e.connect()
        cur=conn.execute("select word,file from Document where word='%s'"%word)
        result=cur.fetchall()
        if len(result)!=0:
          return {word:result[0][1]} 
        else:
            return {word:'Not Found'} 

class Remove(Resource):
    def delete(self, word):
        return {word:'Delete requested'} 


api.add_resource(Index,  '/query/<string:word>')
api.add_resource(Remove, '/delete/<string:word>')
api.add_resource(TodoSimple, '/<string:word><string:doc>')

if __name__ == '__main__':
    app.run(debug=True)
