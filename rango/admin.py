from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register your models here.
# these will be accessible via the web-based admin interface
admin.site.register(Category)
admin.site.register(Page, PageAdmin)

