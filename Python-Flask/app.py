from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Add(Resource):
    def post(self):
        # If Im here, then the resource Add was requested using the method POST

        #Step1: Get posted data
        postedData = request.get_json()
        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        #Step 2: Add the posted data
        ret = x + y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

        
class Subtract(Resource):
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass


api.add_resource(Add, "/add")


#----------------------------------------------------------------
#@app.route('/')
#
#def hello_world():
#    return "Hello World! Learning Flask, now!"




#if __name__==__main__:
#    app.run("host=127.0.0.1", port=80)

app.run(debug=True)