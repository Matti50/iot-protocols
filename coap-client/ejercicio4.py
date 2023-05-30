from time import sleep
import random
import os

cities = ["La_Plata", "Berazategui", "Quilmes"]
motes = [1, 2, 10, 33]

while True:
    city = random.choice(cities)
    mote = random.choice(motes)
    temp = random.randint(14, 31)

    print(f"publishing from coap client: city:{city}, mote: {mote}, temperature: {temp}")

    os.system(f"python coap-client.py -X POST -r climate -b \"climate,localidad={city},mota={mote} temp={temp}\"")
    sleep(10)
