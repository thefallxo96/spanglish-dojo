from django.urls import path
from . import views

urlpatterns = [
    path("", views.lesson_list, name="lesson_list"),
    path("new/", views.lesson_create, name="lesson_create"),
]
