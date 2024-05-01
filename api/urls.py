from django.urls import path
from .views import get_countries, get_cities_by_country

urlpatterns = [
    path('get_countries/', get_countries, name='get_countries'),
    path('get_cities_by_country/<int:id>/', get_cities_by_country, name='get_cities_by_country'),
]