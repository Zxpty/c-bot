import os
from dotenv import load_dotenv

load_dotenv("env_local.env")

class Config:
    TOKEN = os.getenv("KEY")

    if not TOKEN:
        raise RuntimeError("KEY not found in environment variables")

config = Config()