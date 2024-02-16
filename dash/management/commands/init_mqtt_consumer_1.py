from django.core.management.base import BaseCommand
from dash.consumers.consumer_temp_1 import client

class Command(BaseCommand):
    help = 'Init the mqtt consumer'

    def handle(self, *args, **options):
      print('Consumer has started')
      client.username_pw_set('', '')
      client.connect(
          host="test.mosquitto.org",
          port=1883,
          keepalive=60
      )
      client.loop_forever()