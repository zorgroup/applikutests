import time
import os
from multiprocessing import Process, cpu_count

# Load environment variables from a .env file
from dotenv import load_dotenv
load_dotenv()

# Get the DATABASE_URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "Not Set")

# Configure resource usage
CPU_INTENSITY = int(os.getenv("CPU_INTENSITY", 100000))  # Default: 100,000 iterations
RAM_INTENSITY = int(os.getenv("RAM_INTENSITY", 214285714))  # Default: ~6 GB of integers
CPU_PROCESSES = int(os.getenv("CPU_PROCESSES", 8))  # Number of parallel processes

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

# Function to simulate resource usage in parallel
def worker(cpu_intensity, ram_intensity):
    count = 0
    while True:
        count += 1
        # Simulate resource usage
        cpu_result = consume_cpu(cpu_intensity)
        ram_result = consume_ram(ram_intensity)

        # Print the output
        print(f"Worker {os.getpid()}: Iteration {count}, CPU Result: {cpu_result}, RAM Result: {ram_result}")
        time.sleep(2)

if __name__ == "__main__":
    # Start multiple processes to utilize all CPUs
    processes = []
    for _ in range(CPU_PROCESSES):
        p = Process(target=worker, args=(CPU_INTENSITY, RAM_INTENSITY // CPU_PROCESSES))
        p.start()
        processes.append(p)

    # Wait for all processes to finish (infinite loop in this case)
    for p in processes:
        p.join()
