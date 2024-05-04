from rest_framework.decorators import api_view
from rest_framework.response import Response
from cities_light.models import Country, City
from .serializers import CountrySerializer, CitySerializer
from user.models import CustomUser


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


@api_view(['GET'])
def check_for_email_availability(request):
    email = request.GET.get('email')
    print(email)
    if email:
        # Проверяем, существует ли пользователь с заданным email
        try:
            user = CustomUser.objects.get(email=email)
            print(user)
            return Response({'available': False})
        except CustomUser.DoesNotExist:
            return Response({'available': True})
    return Response(status=400)