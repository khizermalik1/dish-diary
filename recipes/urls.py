from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "recipes"

urlpatterns = [
    path(
        "",
        views.RecipeListView.as_view(),
        name="home",
    ),

    path(
        "create/",
        views.create_recipe,
        name="create_recipe",
    ),

    path(
        "recipes/<slug:slug>/edit/",
        views.edit_recipe,
        name="edit_recipe",
    ),

    path(
        "recipes/<slug:slug>/delete/",
        views.delete_recipe,
        name="delete_recipe",
    ),

    path(
        "recipes/<slug:slug>/",
        views.RecipeDetailView.as_view(),
        name="recipe_detail",
    ),

    path(
        "<slug:slug>/comment/",
        views.comment_recipe,
        name="comment_recipe",
    ),

    path(
        "<slug:slug>/like/",
        views.like_recipe,
        name="like_recipe",
    ),

    path(
        "latest-recipes/",
        views.latest_recipes,
        name="latest_recipes",
    ),

    path(
        "search/",
        views.search_recipes,
        name="search_recipes",
    ),

    path(
        "user/<str:username>/",
        views.user_profile,
        name="user_profile",
    ),

    path(
        "profile/edit/",
        views.edit_profile,
        name="edit_profile",
    ),

    path(
        "explore-chefs/",
        views.explore_chefs,
        name="explore_chefs",
    ),

    path(
        "recipes/<slug:slug>/save/",
        views.toggle_favourite,
        name="toggle_favourite",
    ),

    path(
        "favourites/",
        views.saved_recipes,
        name="saved_recipes",
    ),
]
