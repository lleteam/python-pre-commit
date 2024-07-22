import os
from dotenv import load_dotenv

load_dotenv()

def mock_sum(a, b):
    return a + b

def mock_prod(a, b):
    return a * b

def mock_env_var():
    return os.getenv("ENV_VAR")

def mock_secret_var():
    return os.getenv("SECRET_VAR")