import traceback

from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from workerA import add_nums

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://db:27017/test"



api = Api(app)
mongo = PyMongo(app)


class Hello(Resource):
    def get(self):
        return make_response(jsonify({"Hello": "world"}))


class Addtest(Resource):
    def post(self):
        try:
            name = request.json.get("name")
            age = request.json.get("age")
            x = mongo.db.sample.insert({"name": name, "age": age})
            # print(x)
            return jsonify({"user": "added"})
        except:
            print(traceback.format_exc())


class Cel(Resource):
    def post(self):
        try:
            first_num = request.json.get("n1")
            second_num = request.json.get("n2")
            result = add_nums.delay(first_num, second_num)
            print(result)
            return result.id
        except:
            print(traceback.format_exc())


api.add_resource(Hello, '/')
api.add_resource(Addtest, '/add')
api.add_resource(Cel, '/cel')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
