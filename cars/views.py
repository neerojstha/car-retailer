from django.shortcuts import render, get_object_or_404
from .models import Car


def home(request):
    cars = Car.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'cars': cars})


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)

    return render(request, 'car_detail.html', {
        'car': car
    })