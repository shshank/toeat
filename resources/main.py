from flask_restful import Resource
from flask import request

class HelloWorld(Resource):
    def get(self):
        print request
        print request.headers
        print request.data
        return {'hello': 'world'}
