import time
import os
DATABASE_URL = os.environ['hello']

count=1
while True:
    count=count+1
    print("Hello ",count," ", DATABASE_URL)
    time.sleep(2)
