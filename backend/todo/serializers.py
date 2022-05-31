from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # fields contained and converted in JSON data
        fields = ('id', 'title', 'description', 'completed')