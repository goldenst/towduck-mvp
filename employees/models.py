from django.db import models

class Employees(models.Model):
  name = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  citystate = models.CharField(max_length=200)
  zipcode = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  cell = models.CharField(max_length=200)
  cdl = models.CharField(max_length=200)
  hite_date = models.DateField()
  er_contact = models.CharField(max_length=200)
  er_number = models.CharField(max_length=200)
  is_active = models.BooleanField(default=True)
  def __str__(self):
    return self.name

