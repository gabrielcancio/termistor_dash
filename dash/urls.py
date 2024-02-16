from django.urls import path, include
from .views import home, get_data

urlpatterns = [
  path('', home),
  path('data/', get_data)
]
