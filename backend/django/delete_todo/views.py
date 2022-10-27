from django.shortcuts import render, HttpResponse
from . import models
from . import serializers
from rest_framework.generics import DestroyAPIView

class DestroyTodo(DestroyAPIView):
    serializer_class=serializers.TodoSerializer
    queryset=models.Todo.objects.all()



