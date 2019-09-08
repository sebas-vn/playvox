import json
from flask_restful import Resource, Api
from db.db_notes import mongo
from flask import request
from flask import jsonify
from bson import ObjectId
from bson.json_util import dumps
import requests
import datetime

class GetNotesUser(Resource):
	def get(self, id):
		db_notes = mongo.db.note
		users = requests.get(f'http://127.0.0.1:5000/api/v1/user/{id}')
		if(users.status_code == 200):
			note = dumps(db_notes.find({'id_user': ObjectId(id)}))
			return json.loads(note), 200
		else:
			return 'No notes here', 404
		

class CreateNote(Resource):
	def post(self):
		db_notes = mongo.db.note
		req = request.json
		rd = datetime.datetime.now().strftime('%Y-%m-%d')
		req['id_user'] = ObjectId(req['id_user'])
		req['registry_date'] = rd

		db_notes.insert_one(req)
		return 'Note created Successfully', 200