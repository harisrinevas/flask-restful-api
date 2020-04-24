from flask import request, Flask, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient
"""
Includeing comment into the code for git push
"""
app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")

db = client.CustomerDB
cust = db["customer"]

def defError(status, msg):
    return { "status":status, "msg":msg}

def getPasswd(username):
    return cust.find({
        "username":username
    })[0]["password"]

class Register(Resource):
    def post(self):
        req = request.get_json(force=True)

        username = req["username"]
        password = req["password"]

        cust.insert({
            "username": username,
            "password": password
        })

        retJson = defError(200, "User Registered")
        # retJson = {
        #     "status": 200,
        #     "msg": "User Registered"
        # }

        return jsonify(retJson)

class getPass(Resource):
    def get(self):
        req = request.get_json(force=True)
        username = req["username"]

        password = getPasswd(username)

        # password = cust.find({
        #     "username":username
        # })[0]["password"]

        retJson = defError(200, password)
        # retJson = {
        #     "status": 200,
        #     "password":password
        # }

        return jsonify(retJson)

api.add_resource(Register, '/register')
api.add_resource(getPass, '/getPass')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
