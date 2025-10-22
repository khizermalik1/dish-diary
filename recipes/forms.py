from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'summary', 'ingredients',
                  'steps']  # ✅ only real fields
