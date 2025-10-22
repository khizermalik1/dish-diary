from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.RecipeListView.as_view(), name="home"),
    path("create/", views.create_recipe, name="create_recipe"),
    path("recipes/<slug:slug>/edit/", views.edit_recipe, name="edit_recipe"),
    path("recipes/<slug:slug>/delete/",
         views.delete_recipe, name="delete_recipe"),
    path("recipes/<slug:slug>/",
         views.RecipeDetailView.as_view(), name="recipe_detail"),
]
