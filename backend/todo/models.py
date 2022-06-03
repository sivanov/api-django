from pickle import FALSE
from django.db import models

# Notice this Class must be placed before class Todo
# Category table that inherits model.Models
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name # name to be shown when called


class Todo(models.Model):
    # we can write max 200 characters in Title field
    title = models.CharField(max_length = 200)
    description = models.TextField()
    # by default all new created task will be uncompleted
    completed = models.BooleanField(default = False)
    # Foreignkey
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default = 1)
    
    def __str__(self):
        return self.title