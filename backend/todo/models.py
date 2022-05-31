from pickle import FALSE
from django.db import models

class Todo(models.Model):
    # we can write max 200 characters in Title field
    title = models.CharField(max_length = 200)
    description = models.TextField()
    # by default all new created task will be uncompleted
    completed = models.BooleanField(default = False)

    def _str_(self):
        return self.title