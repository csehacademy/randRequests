import requests
import time
import random
i = 0
while i < 5000:
    time.sleep(random.random())
    response = requests.get('https://udemy.com')
    print("csehacademy:",response)
    i = i+1

