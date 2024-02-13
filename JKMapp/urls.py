from django.urls import path
from . import views

urlpatterns = [
        path("", views.mambers, name="index_page"),
        path("Home/", views.Home, name="home")
]

