from rest_framework import serializers
from ..models import Teams

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        # fields = ('id', 'username', 'email', 'password')
        fields = '__all__' #Asi hago lo mismo que arriba