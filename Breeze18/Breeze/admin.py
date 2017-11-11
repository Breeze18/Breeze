from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Profile,Event,Registration,Formdata)
class ProfileAdmin(admin.ModelAdmin):
    pass