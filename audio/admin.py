from django.contrib import admin

# Register your models here.
from .models import Audio, President
admin.site.register(Audio)
admin.site.register(President)