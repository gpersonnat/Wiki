from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("random_page", views.random_page, name="random_page"),
    path("create_page", views.create_page, name="create_page"),
    path("search", views.search, name="search"),
    path("<str:title>", views.display, name="display"),
    path("edit/<str:entry>", views.edit_page, name="edit_page"),
]
