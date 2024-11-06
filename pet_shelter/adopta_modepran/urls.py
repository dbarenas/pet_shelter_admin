# shelter/urls.py
from django.urls import path
from . import views
from .admin import admin_site  # Import your custom admin site

urlpatterns = [
    path('admin/', admin_site.urls),  # Use the custom admin site
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/edit/<int:pk>/', views.edit_animal, name='edit_animal'),

]
