from django.contrib import admin
from django.urls import path, include
from recipes.views import signup_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "",
        include(
            ("recipes.urls", "recipes"),
            namespace="recipes"
        ),
    ),  # namespace wired

    path("signup/", signup_view, name="signup"),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="recipes/login.html"
        ),
        name="login",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(
            next_page="recipes:home"
        ),
        name="logout",
    ),
]
