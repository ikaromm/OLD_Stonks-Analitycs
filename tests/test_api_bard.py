from bardapi import Bard
from dotenv import load_dotenv

import os


def get_api_key() -> dict:
    load_dotenv()

    return {
        "token": os.environ.get("BARD_API_KEY")
    }


def main():
    bard = Bard(**get_api_key())

    resposta = bard.get_answer("Qual a resposta para a vida, o universo e tudo mais?")

    print(resposta['content'])


if __name__ == "__main__":
    main()