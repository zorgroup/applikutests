import time
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Get the DATABASE_URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "Not Set")

count = 1
while True:
    count += 1
    print("Hello ", count, " ", DATABASE_URL)
    time.sleep(2)
