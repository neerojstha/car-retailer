from django.shortcuts import render, get_object_or_404
from .models import Car


def home(request):

    # Get all cars
    cars = Car.objects.all().order_by('-created_at')

    # Get filter values
    brand = request.GET.get('brand')
    year = request.GET.get('year')
    budget = request.GET.get('budget')

    # Apply filters
    if brand:
        cars = cars.filter(brand=brand)

    if year:
        cars = cars.filter(year=year)

    if budget:
        cars = cars.filter(price__lte=budget)

    # Get unique brands
    brands = Car.objects.values_list(
        'brand',
        flat=True
    ).distinct()

    # Get unique years
    years = Car.objects.values_list(
        'year',
        flat=True
    ).distinct().order_by('-year')

    context = {
        'cars': cars,
        'brands': brands,
        'years': years,
    }

    return render(request, 'index.html', context)


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)

    return render(request, 'cars/car_detail.html', {
        'car': car
    })


def contact(request):
    return render(request, "cars/contact.html")


def about(request):
    return render(request, "cars/about.html")