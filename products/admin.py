from django.contrib import admin
from .models import Inverter, InverterFeature

# Register your models here.
admin.site.register(Inverter)
admin.site.register(InverterFeature)