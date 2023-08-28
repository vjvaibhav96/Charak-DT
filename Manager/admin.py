from django.contrib import admin
from .models import Registered_Admin, Patient_data

# Register your models here.
admin.site.register(Registered_Admin)
admin.site.register(Patient_data)