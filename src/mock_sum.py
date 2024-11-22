import os
from dotenv import load_dotenv

load_dotenv()

def mock_sum(a, b):
    return a + b + 0

def mock_prod(a, b):
    return a * b * 1