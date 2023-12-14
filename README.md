# recipefinder-final
 This is a finalised version with the included .gitignore.


# recipefinder-freestyleproject

Create and activate a virtual environment:

## Setup
```sh
conda create -n recipe-helper-env python=3.10

conda activate recipe-helper-env

```

Install packages:
```sh
pip install -r requirements.txt
```

Obtain an [API from Edamam](https://developer.edamam.com/edamam-docs-recipe-api)

Create a ".env" file and paste in the following contents:

# this is the ".env" file...

EDAMAM_API_KEY="_________"
EDAMAM_APP_ID ="_________"

## Usage

Run recipe finder:

```sh
python -m app.recipe_finder
```
Run featured recipes:
```sh
python -m app.featured_recipes
```

## Web

Run the web app (then view in the browser at http://localhost:5000/):

```sh 
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```


## Testing
Run Test:

```sh
pytest
```