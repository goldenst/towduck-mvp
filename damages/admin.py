from django.contrib import admin
from .models import Damage


# Register your models here.
class DamageAdmin(admin.ModelAdmin):
  list_display = ('id', 'customer', 'is_open','status','phone', 'driver', 'cost' )
  list_display_links = ('id', 'customer','phone', 'driver', 'cost' )
  list_filter = ('customer','is_open', )
  list_editable = ('is_open', 'status')
  search_fields = ('customer', 'status')
  list_per_page = 25 

admin.site.register(Damage, DamageAdmin)