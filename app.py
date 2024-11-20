import time
import env  # Import the env package

# Load environment variables
env.read_envfile()  # Reads from a .env file if it exists

# Get the DATABASE_URL from environment variables
DATABASE_URL = env.get("DATABASE_URL", "Not Set")  # Default to "Not Set" if not found

count = 1
while True:
    count += 1
    print("Hello ", count, " ", DATABASE_URL)
    time.sleep(2)
