from django.contrib import admin
from .models import CustomUser, Incident

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Incident)