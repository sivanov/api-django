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
    PRIORITY_LEVELS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

    # we can write max 200 characters in Title field
    title = models.CharField(max_length = 200)
    description = models.TextField()
    # by default all new created task will be uncompleted
    completed = models.BooleanField(default = False)
    # Foreignkey
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default = 1)
    priority = models.CharField(choices=PRIORITY_LEVELS, default = 1, max_length = 20)
    
    def __str__(self):
        return self.title