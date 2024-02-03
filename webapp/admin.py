from django.contrib import admin
from .models import Manufacturer, Category, Product, CPU, GPU, RAM, Storage, PowerSupply, Order



admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(RAM)
admin.site.register(Storage)
admin.site.register(PowerSupply)
admin.site.register(Order)
