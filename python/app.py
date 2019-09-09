from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from resources.note import GetNotesUser, CreateNote
from resources.user import CreateUser, GetUser, DeleteUser, UpdateUser, GetUserOne, GetUserAll

app = Flask(__name__)
CORS(app)
api = Api(app)


""" API NOTES """
api.add_resource(GetNotesUser, '/api/v1/note/<string:id>')
api.add_resource(CreateNote, '/api/v1/note/')

""" API USERS """
api.add_resource(CreateUser, '/api/v1/user/')
api.add_resource(GetUser, '/api/v1/user/')
api.add_resource(GetUserAll, '/api/v1/user/all')
api.add_resource(GetUserOne, '/api/v1/user/<string:id>')
api.add_resource(DeleteUser, '/api/v1/user/delete/<string:id>')
api.add_resource(UpdateUser, '/api/v1/user/update/<string:id>')



if __name__ == '__main__':
	app.run(debug=True)
