import paho.mqtt.client as mqtt
from dash.models import Measurement
from django.utils import timezone

def on_connect(mqtt_client, userdata, flags, rc, properties):
  if rc == 0:
    print('Connected successfully')
    mqtt_client.subscribe('EQ1/temp')
  else:
      print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):
  instant = timezone.now()
  content = msg.payload.decode('utf-8').replace('b', '')
  print(f'Received message on topic: {msg.topic} with payload: {content}')
  Measurement.objects.create(temperature=content, instant=instant, type=0)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message