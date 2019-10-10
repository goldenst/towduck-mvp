from django.db import models
from datetime import datetime
from employees.models import Employees


class Damage(models.Model):
  driver = models.ForeignKey(Employees, on_delete=models.DO_NOTHING)
  date_of_incident = models.DateField()
  call_number = models.IntegerField()
  customer = models.CharField(max_length=50)
  email = models.CharField(max_length=100, blank=True)
  phone = models.CharField(max_length=20)
  vehicle_year = models.IntegerField()
  vehicle_make = models.CharField(max_length=50)
  vehicle_model = models.CharField(max_length=50)
  damages = models.TextField()
  status = models.CharField(max_length=100)
  cost = models.IntegerField(blank=True)
  notes = models.TextField(blank=True)
  date_resolved = models.DateField(blank=True)
  is_open = models.BooleanField(default=True)
  image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  image_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  image_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  image_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  image_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  image_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  entry_date = models.DateTimeField(default=datetime.now)
  def __str__(self):
    return self.customer
