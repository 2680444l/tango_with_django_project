from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
# these will be accessible via the web-based admin interface
admin.site.register(Category)
admin.site.register(Page)