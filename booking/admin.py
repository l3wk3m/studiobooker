from django.contrib import admin
from .models import Studio, StudioBooking

# Register your models here.

admin.site.register(Studio)
admin.site.register(StudioBooking)