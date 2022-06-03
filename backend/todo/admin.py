from django.contrib import admin
from .models import Category, Todo # Django now cant import our Model file

class TodoAdmin(admin.ModelAdmin):
    #  what fields will be visible in our Admin dashboard
    list_display = ('title', 'description', 'completed')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) # notice comma in the end it is mandatory!


# Register your models here.
admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryAdmin)