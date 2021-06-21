from django.contrib import admin
from .models import Produkty, Producent, Kategoria

# Register your models here.

admin.site.register(Produkty)
admin.site.register(Producent)
admin.site.register(Kategoria)