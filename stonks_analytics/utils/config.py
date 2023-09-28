from dotenv import load_dotenv
import os


def load_envs() -> dict:
    load_dotenv()

    return {
        "api_key": os.environ.get("API_KEY")
    }
    