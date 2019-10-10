from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='damages'),
  path('<int: damage_id>', views.damage, name='damage'),
  path('search', views.search, name='search'),
]
