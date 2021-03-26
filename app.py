from flask import Flask, request, jsonify
from restful.models.Recipes import RecipesModel
from restful.models.Desserts import DessertsModel

app = Flask(__name__)

@app.route("/recipes", methods=['GET', 'POST'])
def getRecipes():
	#Se retornan todos los valores de recipes
	if request.method == 'GET':
		return jsonify(RecipesModel().all()), 200
	elif request.method == 'POST':
		return "Aqui es la logica para hacer post"

@app.route("/desserts", methods=['GET', 'POST'])
def getDesserts():
	#Se retornan todos los valores de desserts
	if request.method == 'GET':
		return jsonify(DessertsModel().all()), 200
	elif request.method == 'POST':
		return "Aqui es la logica para hacer post"

if __name__ == '__main__':
	recipes = RecipesController
	app.run(port='5000')