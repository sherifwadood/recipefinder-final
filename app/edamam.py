import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EDAMAM_API_KEY")
APP_ID = os.getenv("EDAMAM_APP_ID")
