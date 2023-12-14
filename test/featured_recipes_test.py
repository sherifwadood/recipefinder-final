from app.featured_recipes import get_featured_recipes

def test_get_featured_recipes():
    print("Testing get_featured_recipes...")

    featured_recipes = get_featured_recipes()
    
    # Basic Functionality Test
    assert isinstance(featured_recipes, list), "Failed: get_featured_recipes should return a list"
    assert len(featured_recipes) == 18, "Failed: get_featured_recipes should return 18 recipes"

    # Content Validation Test
    for recipe in featured_recipes:
        assert 'label' in recipe, "Failed: Each recipe should have a label"
        # Additional checks can be added here for matching labels or other fields

    print("get_featured_recipes...PASSED")

# Call the test function
test_get_featured_recipes()

