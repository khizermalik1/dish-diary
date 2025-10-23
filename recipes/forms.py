from django import forms
from .models import Recipe
from .models import Profile


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'summary', 'ingredients',
                  'steps']   


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']  
