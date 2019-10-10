from django.contrib import admin
from .models import Employees

# Register your models here.
class EmployeesAdmin(admin.ModelAdmin):
  list_display = ('name','is_active', 'cell', 'email', 'er_contact', 'er_number')
  list_display_links = ('name', 'cell')
  search_fields = ('name',)
  list_per_page = 25



admin.site.register(Employees, EmployeesAdmin)