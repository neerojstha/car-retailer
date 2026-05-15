from django.shortcuts import render
from .models import Car


def home(request):
    cars = Car.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'cars': cars})