from django.contrib import admin

# Register your models here.
from .models import VegProduct, NonVegProduct, VeganProduct, Orders

admin.site.register(VegProduct)
admin.site.register(NonVegProduct)
admin.site.register(VeganProduct)
admin.site.register(Orders)