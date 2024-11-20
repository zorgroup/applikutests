import time
import os

# Load environment variables from a .env file
from dotenv import load_dotenv
load_dotenv()

# Get the DATABASE_URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "Not Set")

# Variables to control resource usage
CPU_INTENSITY = int(os.getenv("CPU_INTENSITY", 100000000))  # Number of iterations for CPU
RAM_INTENSITY = int(os.getenv("RAM_INTENSITY", 5000))  # Size of the RAM-consuming list

# Function to consume CPU by performing dummy computations
def consume_cpu(intensity):
    result = 0
    for i in range(1, intensity):
        result += i ** 0.5  # Perform square root calculations
    return result

# Function to consume RAM by creating a large list
def consume_ram(intensity):
    data = [i for i in range(intensity)]  # Create a list with the specified size
    return sum(data)  # Perform a dummy operation to keep it in memory

count = 1
while True:
    count += 1

    # Simulate resource usage
    cpu_result = consume_cpu(CPU_INTENSITY)
    ram_result = consume_ram(RAM_INTENSITY)

    # Print the output
    print(f"Hello {count}, DATABASE_URL: {DATABASE_URL}, CPU Result: {cpu_result}, RAM Result: {ram_result}")

    # Pause for 2 seconds
    time.sleep(2)
