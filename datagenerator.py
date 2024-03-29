import json
import requests
import time
import paho.mqtt.client as mqtt
#Luetaan tiedosto
use_mqtt= True

if use_mqtt:
    broker_address="broker.hivemq.com"

    client = mqtt.Client("Muntunnus")

    client.connect(broker_address)

file = open("mobiledata.txt","r")

for line in file:
    s = json.loads(line)
    if s['channel'] == 'solution':
        pos = s ['position_lcl']

        positionData = {}
        positionData['time'] = s ['time']
        positionData['x'] = pos[0]
        positionData['y'] = pos[1]
        positionData['z'] = pos[2]

        jsonm = json.dumps(positionData, indent=True)
        print(jsonm)
        #lähetetään HTTP:lla
        if False: #omalle palvelinohjellmalle tai Thingspeakiin

            response = requests.post('http://localhost:5000/newmeasurement',data = jsonm)
            print(response)
        if use_mqtt:
            client.publish("my_topicsk",jsonm)
        time.sleep(5)