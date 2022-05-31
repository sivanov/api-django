from django.contrib import admin
from .models import Todo # Django now cant import our Model file

class TodoAdmin(admin.ModelAdmin):
    #  what fields will be visible in our Admin dashboard
    list_display = ('title', 'description', 'completed')

# Register your models here.
admin.site.register(Todo, TodoAdmin)