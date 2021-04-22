from .Model import Model as model
from sqlalchemy import create_engine
import json

class DessertsModel(model):
	def __init__(self):
		model.__init__(self)

	def all(self):
		data = self.db.execute("SELECT * FROM desserts")
		return { "data": [dict(zip(tuple (data.keys()), i)) for i in data.cursor]}

	def create(self, data):
		self.db.execute("INSERT INTO desserts(name, description, can_contain, extras) VALUES (?, ?, ?, ?)", (data['name'], data['description'], json.dumps(data['can_contain']), json.dumps(data['extras'])))
		response = self.db.execute("SELECT * FROM desserts ORDER BY id_dessert DESC LIMIT 1")
		return { "data": [dict(zip(tuple(response.keys()), i)) for i in response.cursor]}

	def delete(self, id_dessert):
		self.db.execute("DELETE FROM desserts WHERE id_dessert = ?", id_dessert)