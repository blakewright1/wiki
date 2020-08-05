from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("random", views.pickrand, name="random"),
    path("search", views.search, name="search"),
    path("<str:name>", views.entry, name="entry"),

]
