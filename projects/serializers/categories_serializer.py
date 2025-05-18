from rest_framework import serializers
from ..models import Categories, CategoriesInfo

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class CategoriesInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesInfo
        fields = '__all__'