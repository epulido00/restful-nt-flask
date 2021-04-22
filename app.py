from flask import Flask, request, jsonify
from models.Recipes import RecipesModel
from models.Desserts import DessertsModel

app = Flask(__name__)

@app.route("/recipes", methods=['GET', 'POST'])
def getRecipes():
	#Se retornan todos los valores de recipes
	if request.method == 'GET':
		return jsonify(RecipesModel().all()), 200
	elif request.method == 'POST':
		return jsonify(RecipesModel().create(request.json)), 200

@app.route("/recipes/<int:id_recipe>", methods=['DELETE'])
def Recipes(id_recipe):
	#Se modifican o borran los valores de recipes
	if request.method == 'DELETE':
		RecipesModel().delete(id_recipe)
		return jsonify(), 200

@app.route("/desserts", methods=['GET', 'POST'])
def getDesserts():
	#Se retornan todos los valores de desserts
	if request.method == 'GET':
		return jsonify(DessertsModel().all()), 200
	elif request.method == 'POST':
		return jsonify(DessertsModel().create(request.json)), 200

@app.route("/desserts/<int:id_dessert>", methods=['DELETE'])
def Desserts(id_dessert):
	#Se modifican o borran los valores de recipes
	if request.method == 'DELETE':
		DessertsModel().delete(id_dessert)
		return jsonify(), 200

if __name__ == '__main__':
	app.run(port='5000')