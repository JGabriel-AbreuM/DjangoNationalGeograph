from django.contrib import admin
from django.urls import path

app_name = "Animal"

urlpatterns = [
    path('admin/', admin.site.urls),
]
