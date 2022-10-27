from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:pk>/', views.DestroyTodo.as_view())
]
