from django.contrib import admin
from .models import Car, CarImage, HeroSlide


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 15


class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]


admin.site.register(Car, CarAdmin)
admin.site.register(HeroSlide)