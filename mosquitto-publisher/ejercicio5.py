import paho.mqtt.publish as publish
import random
from time import sleep
import json

cities = ["La_Plata", "Berazategui", "Quilmes"]
motes = [1, 2, 10, 33]

while True:
    city = random.choice(cities)
    mote = random.choice(motes)
    temp = random.randint(14, 31)
    payload_data = {
        "localidad": city,
        "mota": mote,
        "temp": temp
    }

    payload = json.dumps(payload_data)

    print(f"publishing from mosquitto client. Data: {payload}")

    publish.single("temperatura", payload)
    sleep(10)
