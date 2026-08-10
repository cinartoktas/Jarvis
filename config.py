from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

BASE_URL = "https://openrouter.ai/api/v1"

MODEL = "openrouter/free"

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")