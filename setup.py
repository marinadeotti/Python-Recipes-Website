from flask import Flask, render_template, request

import requests


app = Flask(__name__)

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

headers = {
  'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
  'x-rapidapi-key': "743f5fbf79msh54ef0a5008c5278p122dcajsn341602cc2807",
  }

findByRecipe = "recipes/complexSearch"
findByIngredients = "recipes/findByIngredients"
findByNutrients = "recipes/findByNutrients"
# randomFind = "recipes/random"

@app.route('/')
def search_page():
  return render_template('search.html')

@app.route('/recipes')
def get_recipes():

  if (str(request.args['recipe']).strip() != ""):
    querystring = {"number":"12","ingredients":request.args['recipe']}
    response = requests.request("GET", url + findByIngredients, headers=headers, params=querystring).json()
    return render_template('recipes.html', recipes=response)

  else:
    print("No recipes found.")

@app.route('/ingredients')
def get_ingredients():

  if (str(request.args['ingredients']).strip() != ""):
    querystring = {"number":"12","ranking":"1","ingredients":request.args['ingredients']}
    response = requests.request("GET", url + findByIngredients, headers=headers, params=querystring).json()
    return render_template('recipes.html', recipes=response)
      
  else:
    print("No recipes found.")

@app.route('/nutrients')
def get_nutrients():
      
  if (str(request.args['minProtein']).strip() != ""):
    querystring = {"number":"12","ranking":"1","minProtein":request.args['minProtein'], "minCarbs":request.args['minCarbs'], "minFat":request.args['minFat']}      
    response = requests.request("GET", url + findByNutrients, headers=headers, params=querystring).json()
    return render_template('recipes.html', recipes=response)
      
  else:
    print("No recipes found.")

@app.route('/recipe')
def get_recipe():
  recipe_id = request.args['id']
  recipe_info_endpoint = "recipes/{0}/information".format(recipe_id)
  similar = "recipes/{0}/similar".format(recipe_id)
  # equipmentWidget = "recipes/{0}/equipmentWidget.json".format(recipe_id)

  recipe_info = requests.request("GET", url + recipe_info_endpoint, headers=headers).json()
    
  recipe_headers = {
      'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
      'x-rapidapi-key': "743f5fbf79msh54ef0a5008c5278p122dcajsn341602cc2807",
  }
  querystring = {"number":"4"}
  recipe_info['similar'] = requests.request("GET", url + similar, headers=recipe_headers, params=querystring).text
  
  # recipe_info['equipmentWidget'] = requests.request("GET", url + equipmentWidget, headers=recipe_headers, params=querystring).text

  return render_template('recipe.html', recipe=recipe_info)
    

if __name__ == '__main__':
  app.run()