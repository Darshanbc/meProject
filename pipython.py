import time
import paho.mqtt.client as mqtt
import ssl
import json


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))


client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(ca_certs='/home/pi/CA-cert.pem.crt', certfile='/home/pi/4934b462ce-certificate.pem.crt', keyfile='/home/pi/4934b462ce-private.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("a107juxensv3gm.iot.ap-southeast-1.amazonaws.com", 8883, 60) 

key0='patientId'
value0='1'

key1='ocontent'
value1='98'

key2='bp'
value2='127-98'

key3='ecg'
value3='[1234,5674,8762,982,6867]'

key4='weight'
value4='75'
msg={key0:value0,key1:value1,key2:value2,key3:value3,key4:value4}

jmsg=json.dumps(msg)
def senddata():
     client.publish("patient/diagdata", payload=jmsg , qos=1, retain=False)



while True:
 incode=raw_input("Would you like to send data now to cloud? Y/N\nPress R to reconnect\n")
 if incode=='Y':
  client.reconnect()
  senddata()
else: 
  sleep(10)

    
#client.loop_forever()
