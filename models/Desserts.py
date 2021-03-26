from restful.models.Model import Model as model
from sqlalchemy import create_engine

class DessertsModel(model):

	table = 'desserts'
	fillable = ['name', 'description', 'can_contain', 'extras']

	def __init__(self):
		model.__init__(self)

	def all(self):
		data = self.db.execute("SELECT * FROM desserts")
		return { "desserts": [dict(zip(tuple (data.keys()), i)) for i in data.cursor]}