from restful.models.Model import Model as model
from sqlalchemy import create_engine

class RecipesModel(model):

	table = 'recipes'
	fillable = ['name', 'description', 'ingredients', 'preparation']

	def __init__(self):
		model.__init__(self)

	def all(self):
		data = self.db.execute("SELECT * FROM recipes")
		return { "recipes": [dict(zip(tuple (data.keys()), i)) for i in data.cursor]}

	def create(self, data):
		response = self.db.execute("INSERT INTO recipes(name, description, ingredients, preparation) VALUES ({0}, {1}, {2}, {3})".format(data['name'], data['description'], json.dump(data['ingredients']), json.dump(data['preparation'])));
		return { "recipes": [dict(zip(tuple (response.keys()), i)) for i in response.cursor]}