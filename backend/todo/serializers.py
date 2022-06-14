from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    # replace category ID in Database with actual human readable name
    category = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Todo
        # fields contained and converted in JSON data
        fields = ('id', 'title', 'category', 'description', 'completed', 'priority')