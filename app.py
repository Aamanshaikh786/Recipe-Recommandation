from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["recipe_db"]
collection = db["recipes"]

# --------------------------
# Recommendation Function
# --------------------------
def get_recommendations(user_ingredients):
    user_set = set([i.lower().strip() for i in user_ingredients])
    recipes = list(collection.find())

    # Calculate match score & total ingredients
    for recipe in recipes:
        recipe_set = set(recipe.get("Cleaned_Ingredients", []))
        recipe["match_score"] = len(user_set.intersection(recipe_set))
        recipe["total_ingredients"] = len(recipe.get("Cleaned_Ingredients", []))

    # First, filter top matches (e.g., top 5 by match score)
    top_recipes = sorted(recipes, key=lambda x: x["match_score"], reverse=True)[:5]

    # Now sort those top recipes by ascending total ingredients
    top_recipes_sorted = sorted(top_recipes, key=lambda x: x["total_ingredients"])

    return top_recipes_sorted

# --------------------------
# Flask Routes
# --------------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user ingredients from form input
    user_input = request.form['ingredients']
    user_ingredients = [i.strip() for i in user_input.split(',')]

    # Get top recommendations
    recommendations = get_recommendations(user_ingredients)

    return render_template('results.html', ingredients=user_ingredients, recipes=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
