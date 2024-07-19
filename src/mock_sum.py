from dotenv import load_dotenv
import os

load_dotenv()

def mock_sum(a, b):
    print(f"SECRET: {os.getenv('SECRET')}")
    return a + b + 1
