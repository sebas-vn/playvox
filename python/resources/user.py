import json
from flask_restful import Resource, Api
from db.db_users import mongo
from flask import request
from flask import jsonify
from bson import ObjectId
from bson.json_util import dumps
import datetime

class GetUser(Resource):
	def get(self):
		db_user = mongo.db.user
		query_search = request.args.get('query')
		users = dumps(db_user.find(json.loads(query_search)))

		if(users):
			return json.loads(users), 200
		else:
			return 'No users here', 404


class GetUserAll(Resource):
	def get(self):
		db_user = mongo.db.user
		users = dumps(db_user.find())

		if(users):
			return json.loads(users), 200
		else:
			return 'No users here', 404



class GetUserOne(Resource):
	def get(self, id):
		db_user = mongo.db.user
		user = dumps(db_user.find_one({'_id': ObjectId(id)}))

		if (user):
			return json.loads(user), 200
		else:
			return 'No users here', 404


class CreateUser(Resource):
	def post(self):
		db_user = mongo.db.user
		req = request.json
		response = ''
		if (isinstance(req, list)):
			for user in req:
				verify_user = db_user.find_one({'email' : req['email']})
				if not verify_user:
					db_user.insert_one(req)
					response = {'status': 201, 'message': 'User created succesfully!'}
				else:
					response = 'User already exists', 400
		else:
			verify_user = db_user.find_one({'email' : req['email']})
			if not verify_user:
				rd = datetime.datetime.now().strftime('%Y-%m-%d')
				req['registry_date'] = rd
				db_user.insert_one(req)
				response = 'User created succesfully!', 201
			else:
				response = 'User already exists', 400

		return response


class DeleteUser(Resource):
	def put(self, id):
		db_user = mongo.db.user
		user = db_user.find_one({'_id': ObjectId(id)})

		if(user):
			db_user.delete_one(user)
			response = {'status': 200, 'message': 'Deleted successfully'}
		else:
			response = {'status': 400, 'message': 'User does not exist'}

		return response


class UpdateUser(Resource):
	def put(self, id):
		db_user = mongo.db.user
		req = request.json
		user = db_user.find_one({'_id': ObjectId(id)})

		if(user):
			db_user.update_one({'_id': ObjectId(id)}, {'$set': req})
			return 'User updated successfully', 200
		else:
			return 'User does not exist', 404
