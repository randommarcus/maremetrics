from dotenv import load_dotenv
import os

load_dotenv()

ARGOVIS_API_KEY = os.getenv("ARGOVIS_API_KEY")

ARGOVIS_BASE_URL = os.getenv(
    "ARGOVIS_BASE_URL",
    "https://argovis-api.colorado.edu"
)