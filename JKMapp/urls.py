from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
        path("", views.Home, name="home")
] + staticfiles_urlpatterns()
