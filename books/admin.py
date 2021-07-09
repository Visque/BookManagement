from django.contrib import admin
from .models import BookInfo

# Register your models here.
admin.site.register(BookInfo)                   # Enabling admin privileges to the Model BookInfo so that it can be registered for admins