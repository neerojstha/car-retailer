from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Car, HeroSlide

def home(request):

     # HERO SLIDES
    slides = HeroSlide.objects.filter(active=True)

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
        'slides': slides,
    }

    

    return render(request, 'index.html', context)


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)

    return render(request, 'cars/car_detail.html', {
        'car': car
    })



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        # Validate required fields
        if not name or not email or not message:
            messages.error(
                request,
                "Please complete your name, email and message."
            )
            return render(request, "cars/contact.html")

        # Prevent excessively long submissions
        if (
            len(name) > 100
            or len(email) > 254
            or len(phone) > 30
            or len(message) > 5000
        ):
            messages.error(
                request,
                "One or more fields are too long."
            )
            return render(request, "cars/contact.html")

        subject = f"Motorhive website enquiry from {name}"

        email_message = (
            f"Name: {name}\n"
            f"Customer email: {email}\n"
            f"Phone: {phone or 'Not provided'}\n\n"
            f"Message:\n{message}"
        )

        try:
            send_mail(
                subject=subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["sales@motorhive.ie"],
                fail_silently=False,
                reply_to=[email],
            )

        except Exception:
            messages.error(
                request,
                "Sorry, we could not send your message. "
                "Please email sales@motorhive.ie directly."
            )
            return render(request, "cars/contact.html")

        messages.success(
            request,
            "Thank you! Your enquiry has been sent successfully."
        )
        return redirect("contact")

    return render(request, "cars/contact.html")



def about(request):
    return render(request, "cars/about.html")