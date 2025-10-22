from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.http import HttpResponseForbidden
from .models import Recipe
from .forms import RecipeForm


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
    queryset = Recipe.objects.order_by('-created_at')


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'recipes/signup.html', {'form': form})


@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # ✅ correct field
            recipe.save()
            return redirect('recipes:home')
    else:
        form = RecipeForm()
    return render(request, 'recipes/create_recipe.html', {'form': form})


@login_required
def edit_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.user != recipe.author and not request.user.is_superuser:
        return HttpResponseForbidden("You can't edit this recipe.")

    form = RecipeForm(request.POST or None, instance=recipe)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('recipes:home')

    return render(request, 'recipes/edit_recipe.html', {'form': form})


@login_required
def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.user == recipe.author or request.user.is_superuser:
        recipe.delete()
        return redirect('recipes:home')
    return HttpResponseForbidden("You can't delete this recipe.")
