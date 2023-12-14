import requests
from app.edamam import API_KEY, APP_ID

def fetch_recipe(query):
    request_url = f"https://api.edamam.com/api/recipes/v2?type=public&q={query}&app_id={APP_ID}&app_key={API_KEY}&field=label&field=image&field=url&field=totalNutrients"
    response = requests.get(request_url)
    return response.json() if response.status_code == 200 else None

def get_featured_recipes():
    featured_dishes = [
        "Chicken Milanese", "Lamb Chops", "Banana Bread", "Espresso Martini",
        "Chicken Fried Rice", "Beef Wellington", "Michelada", 
        "Spaghetti and Meatballs", "Lentil Soup", "Chocolate Chip Cookies", 
        "Eggs Benedict", "Ratatouille", "Pad Thai", "Quiche Lorraine", "Caprese Salad", "Gazpacho", "Octopus", "Chicken Caesar Salad"
    ]
    featured_recipes = []
    for dish in featured_dishes:
        recipe = fetch_recipe(dish)
        if recipe:
            featured_recipes.append(recipe['hits'][0]['recipe'])  # Assuming first hit is the most relevant
    return featured_recipes