import os
from dotenv import load_dotenv

load_dotenv()

def mock_sum(a, b):
    print(f"SECRET: {os.getenv('SECRET')}")
    return a + b
