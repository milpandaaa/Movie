from django.contrib import admin
from .models import *
models = [Profile, Сassette, Seller, Selling, Admission]
admin.site.register(models)
# Register your models here.
