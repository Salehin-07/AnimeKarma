from django.contrib import admin
from django.urls import path
from aninews import views  # Use lowercase app name

urlpatterns = [
    path("", views.home, name='home'),
    path('admin/', admin.site.urls),
]