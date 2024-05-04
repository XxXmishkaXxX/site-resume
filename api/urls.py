from django.urls import path
from .views import get_countries, get_cities_by_country, check_for_email_availability

urlpatterns = [
    path('get_countries/', get_countries, name='get_countries'),
    path('get_cities_by_country/<int:id>/', get_cities_by_country, name='get_cities_by_country'),
    path('check_for_email_availability/', check_for_email_availability, name='check_email_availability'),
]