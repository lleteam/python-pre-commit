import os
from dotenv import load_dotenv

load_dotenv()


def mock_sum(a, b):
    print(f"SECRET: {os.getenv('SECRET')}")
    print(f"NO SECRET: {os.getenv('NO_SECRET')}")
    return a + b + 1