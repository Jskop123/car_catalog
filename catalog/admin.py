from django.contrib import admin
from .models import Index, Car, Order, OrderedCar, Contact

admin.site.register(Index)
admin.site.register(Car)
admin.site.register(Order)
admin.site.register(OrderedCar)
admin.site.register(Contact)
# Register your models here.
