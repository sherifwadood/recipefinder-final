# This is the "test/recipe_finder_test.py" file...

from app.recipe_finder import fetch_recipes

def test_fetch_recipes():
    print("Testing fetch_recipes...")

    # Test with valid ingredients
    ingredients = ["chicken", "rice"]
    result = fetch_recipes(ingredients)
    assert result is not None, "Failed: fetch_recipes should not return None for valid ingredients"
    assert "hits" in result, "Failed: 'hits' not in response for valid ingredients"
    print("fetch_recipes with valid ingredients...PASSED")

def test_no_ingredients():
    print("Testing fetch_recipes with no ingredients...")

    ingredients = []
    result = fetch_recipes(ingredients)
    assert result is None or "hits" not in result or len(result["hits"]) == 0, "Failed: fetch_recipes should return None or empty 'hits' for no ingredients"
    print("fetch_recipes with no ingredients...PASSED")


# Call the test functions
test_fetch_recipes()
test_no_ingredients()

