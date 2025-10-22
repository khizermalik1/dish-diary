from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author']
        fields = ['title', 'summary', 'is_published']
