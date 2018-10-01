import paho.mqtt.client as paho
import os
from time import sleep
import socket
import ssl
import json

#key1="patientid"
#value1=4

#key2="bp"
#value2="127-90"

#rawmsg={key1:value1,key2:value2}
#msg=json.dumps(rawmsg)

def on_connect(client,userdata,flags,rc):
	if rc==0:	
	 print("Connected successful"+str(rc))
	elif rc==1:
	 print("Connection falied:"+str(rc))

def on_message(client, userdata, msgs):
	print(msgs.topic+" "+str(msgs.payload))

mqttc=paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message=on_message

awshost = "a107juxensv3gm.iot.ap-southeast-1.amazonaws.com"
clientID = "Raspberry-pi"
capath = "/home/pi/CA-cert.pem"
certpath = "/home/pi/8c6edc46e8-certificate.pem.crt"
keypath = "/home/pi/8c6edc46e8-private.pem.key"

mqttc.tls_set(capath, certfile=certpath, keyfile=keypath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost,port=8883, keepalive=60)
while True:
	mqttc.publish("$aws/things/Raspberry-pi/shadow/update/diagdata",payload= "msg",qos=1)
	sleep(10)
mqttc.loop_forever()

