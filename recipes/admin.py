from django.contrib import admin
from .models import Recipe, Comment, Like, Favourite, Profile

admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Favourite)
admin.site.register(Profile)
