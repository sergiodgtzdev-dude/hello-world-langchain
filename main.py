import os

from dotenv import load_dotenv

load_dotenv(".env")

OPEN_AI_API_KEY = os.environ.get("OPENAI_API_KEY")
print(OPEN_AI_API_KEY)


def main():
    print("Hello from langchain-course!")


if __name__ == "__main__":
    main()
