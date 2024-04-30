from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from cities_light.models import Country, City
from .serializers import CountrySerializer, CitySerializer


@api_view(['GET'])
def get_countries(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_cities_by_country(request, id):
    cities = City.objects.filter(country_id=id)
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)
