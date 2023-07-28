from django.contrib import admin
from .models import Booking, Drinks, DrinksCategory, Employees

# Register your models here.
admin.site.register(Booking)
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
admin.site.register(Employees)