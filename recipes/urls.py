from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='home'),
    path('recipes/<slug:slug>/',
         views.RecipeDetailView.as_view(), name='recipe_detail'),
]
