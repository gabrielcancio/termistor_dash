from django.utils import timezone
from ..models import Measurement

def saveMeasuremnt(payload, type):
  instant = timezone.now()
  content = decode(payload)
  Measurement.objects.create(temperature=content, instant=instant, type=type)

  def decode(payload):
    return payload.decode('utf-8').replace('b', '')