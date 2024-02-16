from django.db import models

# Create your models here.
class Measurement(models.Model):
  temperature = models.CharField(max_length=5)
  instant = models.DateTimeField(null=True)
  type = models.IntegerField(null=True)