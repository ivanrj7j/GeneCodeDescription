from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
# api keys and other sensitive content is stored in .env file 

GEMINI_MODEL_NAME = "models/gemini-2.5-pro-exp-03-25"