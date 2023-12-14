# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template
from app.recipe_finder import fetch_recipes
from app.featured_recipes import get_featured_recipes  

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    featured_recipes = get_featured_recipes()  # Fetch featured recipes
    return render_template("home.html", featured_recipes=featured_recipes)

@home_routes.route("/about")
def about():
    print("ABOUT...")
    #return "About Me"
    return render_template("about.html")

@home_routes.route("/recipes", methods=["GET", "POST"])
def recipes():
    if request.method == "POST":
        # Get ingredients and filters from form
        ingredients = request.form.get("ingredients")
        dish_type = request.form.get("dishType")
        meal_type = request.form.get("mealType")

        # Split ingredients into a list
        ingredients_list = ingredients.split(',') if ingredients else []

        # Fetch recipes using the API with filters
        recipes_data = fetch_recipes(ingredients_list, dish_type, meal_type)

        # Render the recipes template with the data
        return render_template("recipes_results.html", recipes=recipes_data["hits"])
    else:
        # Redirect to home if not a POST request
        return render_template("recipe_search.html")