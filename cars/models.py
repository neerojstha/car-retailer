from django.db import models
from django.utils import timezone


class Car(models.Model):
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/')

    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# NEW MODEL
class CarImage(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(upload_to='car_gallery/')

    def __str__(self):
        return f"{self.car.title} Image"

# Hero Model
class HeroSlide(models.Model):

    title = models.CharField(max_length=200)

    subtitle = models.TextField()

    image = models.ImageField(
        upload_to='hero_images/',
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to='hero_videos/',
        blank=True,
        null=True
    )

    button_text = models.CharField(
        max_length=100,
        default="Explore Cars"
    )

    button_link = models.CharField(
        max_length=200,
        default="#cars"
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title        