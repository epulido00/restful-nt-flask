from restful.models.Model import Model as model
from sqlalchemy import create_engine
import json

class RecipesModel(model):
	def __init__(self):
		model.__init__(self)

	def all(self):
		data = self.db.execute("SELECT * FROM recipes")
		return { "data": [dict(zip(tuple (data.keys()), i)) for i in data.cursor]}

	def create(self, data):
		self.db.execute("INSERT INTO recipes(name, description, ingredients, preparation) VALUES (?, ?, ?, ?)", (data['name'], data['description'], json.dumps(data['ingredients']), json.dumps(data['preparation'])))
		response = self.db.execute("SELECT * FROM recipes LIMIT 1 ORDER BY id_recipe DESC")
		return { "data": [dict(zip(tuple (response.keys()), i)) for i in response.cursor]}

	def delete(self, id_recipe):
		self.db.execute("DELETE FROM recipes WHERE id_recipe = ?", id_recipe)