from .models import UserProfile
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    city_name = serializers.SerializerMethodField()
    country_name = serializers.SerializerMethodField()
    def get_city_name(self, obj):
        return obj.city.name if obj.city else None

    def get_country_name(self, obj):
        return obj.country.name if obj.country else None

    class Meta:
        model = UserProfile
        fields = ['full_name', 'city_name', 'country_name',
                  'bio', 'avatar', 'birth_date']
