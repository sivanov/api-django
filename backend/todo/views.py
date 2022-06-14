from django.shortcuts import render
# base class provides the implementation for CRUD operations by default
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
# for search 
from rest_framework import filters
from rest_framework import generics

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

# http://127.0.0.1:8000/api/v1/q/?search=todo
class TodoSearchListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter]
    # search in 1 or more field in DB. Required to be CharField or TextField.
    search_fields = ['title', 'description']