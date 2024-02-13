from django.urls import path
from . import views

urlpatterns = [
        path("", views.mambers, name="Home"),
        path("Home/", views.Home, name="Home")
]

