from django.contrib import admin
from .models import SchoolClass, ClassSheet

# Register your models here.
admin.site.register([SchoolClass, ClassSheet])