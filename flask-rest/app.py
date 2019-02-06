'''
Article: [This is how easy it is to create a REST API](https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3)
Original code: https://gist.github.com/leon-sleepinglion/97bfd34132394e23ca5905ec730f776a
'''

from flask import Flask
from flask_restful import Api, Resource, reqparse # pylint: disable=no-name-in-module,import-error
import os

app = Flask(__name__)
api = Api(app)

services = [
    {
        "name": "authorization",
        "lang": "python",
        "version": "1.1.0"
    },
    {
        "name": "notification",
        "lang": "python",
        "version": "1.0.1"
    },
    {
        "name": "gateway",
        "lang": "nodejs",
        "version": "2.5.14"
    }
]

class ListServices(Resource):
    def get(self):
        return services, 200

class Service(Resource):
    def get(self, name):
        for service in services:
            if(name == service["name"]):
                return service, 200
        return "Service not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("lang")
        parser.add_argument("version")
        args = parser.parse_args()

        for service in services:
            if(name == service["name"]):
                return "User with name {} already exists".format(name), 400

        service = {
            "name": name,
            "lang": args["lang"],
            "version": args["version"]
        }
        services.append(service)
        return service, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("lang")
        parser.add_argument("version")
        args = parser.parse_args()

        for service in services:
            if(name == service["name"]):
                service["lang"] = args["lang"]
                service["version"] = args["version"]
                return service, 200

        service = {
            "name": name,
            "lang": args["lang"],
            "version": args["version"]
        }
        services.append(service)
        return service, 201

    def delete(self, name):
        global services
        services = [service for service in services if service["name"] != name]
        return "{} is deleted.".format(name), 200

class Get_status(Resource):
    def get(self):
        status = { 'Application name': app_name, 'Version': __version__, 'Environment': os.getenv('ENVIRONMENT', 'None') }
        return status, 200

app_name='flask-rest'
__version__='1.0'
debug=False

exec(open("./version.py").read())

api.add_resource(ListServices, "/service")
api.add_resource(Service, "/service/<string:name>")
api.add_resource(Get_status, "/status")

app.run(debug=debug)
