from django.contrib import admin
from myloader.models import MyImage, Category
# Register your models here.


@admin.register(MyImage)
class MyImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Category)
class MyCategoryAdmin(admin.ModelAdmin):
    list_display = ['id']
