from flask_restful import Resource

# 例：
class Cat(Resource):

    def get(self):
        return {'message':'get'}
    def put(self):
        return {'message':'put'}



