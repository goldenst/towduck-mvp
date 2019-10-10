from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Damage


def index(request):
  damages = Damage.objects.all()

  paginator = Paginator(damages, 3)
  page = request.GET.get('page')
  paged_damages = paginator.get_page(page)

  context = {
    'damages': paged_damages
  }

  return render(request, 'damages/damages.html', context)

def damage(request):
  return render(request, 'damages/damage.html')

def search(request):
  return render(request, 'damages/search.html')