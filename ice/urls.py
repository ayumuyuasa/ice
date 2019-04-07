from django.urls import path, include

from django.contrib import admin

urlpatterns = [
    path('', include('item.urls')),

    path('admin/', admin.site.urls),
]
