import time
import os
import environ
DATABASE_URL = os.environ['DATABASE_URL']

count=1
while True:
    count=count+1
    print("Hello ",count," ", DATABASE_URL)
    time.sleep(2)
