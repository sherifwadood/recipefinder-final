from flask import Blueprint, render_template
from app.featured_recipes import get_featured_recipes

featured_recipes_routes = Blueprint('featured_recipes_routes', __name__)

@featured_recipes_routes.route('/featuredrecipes')
def show_all_featured():
    featured_recipes = get_featured_recipes()  # Fetch the featured recipes
    return render_template('featured_recipes.html', featured_recipes=featured_recipes)