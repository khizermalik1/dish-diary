from .models import Recipe, Favourite
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count
from .models import Recipe, Comment, Like
from .forms import RecipeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
    queryset = Recipe.objects.annotate(
        comment_count=Count('comments'),
        like_count=Count('likes')
    ).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular_recipes'] = Recipe.objects.annotate(
            comment_count=Count('comments'),
            like_count=Count('likes')
        ).order_by('-like_count')[:4]
        return context


class RecipeDetailView(SuccessMessageMixin, generic.DetailView):
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
            recipe.author = request.user
            recipe.save()
            messages.success(request, "✅ Recipe created successfully!")
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
        messages.success(request, "✏️ Recipe updated successfully!")
        return redirect('recipes:recipe_detail', slug=recipe.slug)
    return render(request, 'recipes/edit_recipe.html', {'form': form})


@login_required
def delete_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.user == recipe.author or request.user.is_superuser:
        recipe.delete()
        messages.success(request, "🗑️ Recipe deleted successfully!")
        return redirect('recipes:home')
    return HttpResponseForbidden("You can't delete this recipe.")


@login_required
def comment_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == 'POST':
        Comment.objects.create(
            recipe=recipe,
            author=request.user,
            body=request.POST.get('body')
        )
        messages.success(request, "💬 Comment submitted successfully!")
    return redirect('recipes:recipe_detail', slug=slug)


@login_required
def like_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    Like.objects.get_or_create(recipe=recipe, user=request.user)
    messages.success(request, "❤️ You liked this recipe!")
    return redirect('recipes:recipe_detail', slug=slug)


def latest_recipes(request):
    page = int(request.GET.get('page', 1))
    recipes = Recipe.objects.annotate(
        comment_count=Count('comments'),
        like_count=Count('likes')
    ).order_by('-created_at')[(page-1)*10:page*10]
    return render(request, 'recipes/latest_recipes_chunk.html', {'recipes': recipes})


def search_recipes(request):
    query = request.GET.get('q', '')
    results = Recipe.objects.annotate(
        comment_count=Count('comments'),
        like_count=Count('likes')
    ).filter(
        Q(title__icontains=query) |
        Q(summary__icontains=query) |
        Q(ingredients__icontains=query) |
        Q(author__username__icontains=query)
    ).order_by('-created_at')
    return render(request, 'recipes/search_results.html', {'query': query, 'results': results})


def user_profile(request, username):
    user_obj = get_object_or_404(User, username=username)
    recipes = Recipe.objects.filter(author=user_obj).annotate(
        comment_count=Count('comments'),
        like_count=Count('likes')
    ).order_by('-created_at')
    return render(request, 'recipes/user_profile.html', {
        'profile_user': user_obj,
        'recipes': recipes
    })


@login_required
def edit_profile(request):
    # Ensure profile exists
    profile, created = Profile.objects.get_or_create(user=request.user)

    form = ProfileForm(request.POST or None,
                       request.FILES or None, instance=profile)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "📝 Profile updated successfully!")
        return redirect('recipes:user_profile', username=request.user.username)
    return render(request, 'recipes/edit_profile.html', {'form': form})


def explore_chefs(request):
    users = User.objects.all().order_by('username')
    return render(request, 'recipes/explore_chefs.html', {'users': users})


@login_required
def toggle_favourite(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    fav, created = Favourite.objects.get_or_create(
        user=request.user, recipe=recipe)
    if not created:
        fav.delete()
    return redirect('recipes:recipe_detail', slug=slug)


@login_required
def saved_recipes(request):
    saved = Favourite.objects.filter(
        user=request.user).select_related('recipe')
    return render(request, 'recipes/saved_recipes.html', {'saved': saved})
