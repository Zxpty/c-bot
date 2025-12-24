import os
from dotenv import load_dotenv

load_dotenv("env_local.env")

class Config:
    TOKEN = os.getenv("KEY")
    GUILD_ID = 1310814995013046315

    if not TOKEN:
        raise RuntimeError("KEY not found in environment variables")

config = Config()