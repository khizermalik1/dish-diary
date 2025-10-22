from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),  # ✅ this line connects your app
    # optional, for login/logout
    path('accounts/', include('django.contrib.auth.urls')),
]
