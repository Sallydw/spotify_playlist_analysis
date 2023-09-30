import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file


@dataclass
class Env:
    OPEN_AI_KEY: str = os.getenv('OPEN_AI_KEY')
