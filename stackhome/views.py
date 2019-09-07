from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Apartment


# Create your views here.


# def index(request):
#     apartements = Apartment.objects.all()
#     return render(request, 'stackhome/index.html', {'apartments': apartements})
class IndexView(generic.ListView):
    template_name = 'stackhome/index.html'
    context_object_name = 'apartments'

    def get_queryset(self):
        return Apartment.objects.all()


# def detail(request, apartment_id):
#     apartment = get_object_or_404(Apartment, id=apartment_id)
#     return render(request, 'stackhome/detail.html', {'apartment' : apartment})
class DetailView(generic.DetailView):
    template_name = 'stackhome/detail.html'
    context_object_name = 'apartment'
    model = Apartment
