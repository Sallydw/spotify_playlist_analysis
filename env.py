import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file


@dataclass
class Env:
    OPEN_AI_KEY: str = os.getenv('OPEN_AI_KEY')
    SPOTIPY_CLIENT_ID: str = os.getenv('SPOTIPY_CLIENT_ID')
    SPOTIPY_CLIENT_SECRET: str = os.getenv('SPOTIPY_CLIENT_SECRET')

    
