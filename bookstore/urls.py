from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # User management
    path('accounts/', include('allauth.urls')),

    # path('accounts/', include('users.urls')), 
    path('', include('pages.urls')),
]
