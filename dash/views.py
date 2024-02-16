from django.shortcuts import render
from django.http import JsonResponse
from .models import Measurement

# Create your views here.
def home(request):
  measurements = get_measurements()
  return render(request, "index.html", {"measurements": measurements})

def get_data(request):
  measurements = get_measurements()
  return JsonResponse(measurements, safe=False)

def get_measurements():
  return list(Measurement.objects.all().values('temperature', 'id', 'instant', 'type'))