from django.contrib import admin
from .models import RunRegister, FailuresList, CategoryList

# Register your models here.
admin.site.register(RunRegister)
admin.site.register(FailuresList)
admin.site.register(CategoryList)
