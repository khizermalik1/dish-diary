from django.views import generic
from .models import Recipe
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "recipes/home.html")


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
    queryset = Recipe.objects.filter(is_published=True).order_by('-created_at')


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
    queryset = Recipe.objects.filter(is_published=True).order_by('-created_at')
