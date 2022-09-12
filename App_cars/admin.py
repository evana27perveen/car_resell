from django.contrib import admin
from App_cars.models import CarModel, BlogModel, Review


# Register your models here.
class CarModelAdmin(admin.ModelAdmin):
    search_fields = ("name", "status")


admin.site.register(CarModel, CarModelAdmin)
admin.site.register(BlogModel)
admin.site.register(Review)
