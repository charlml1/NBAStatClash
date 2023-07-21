from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("categories/", views.categories, name="categories"),
path("points/", views.points, name="points"),
]