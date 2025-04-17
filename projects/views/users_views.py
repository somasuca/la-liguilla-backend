from rest_framework import viewsets,permissions, status
from ..serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getUsers(request):
    users = User.objects.all()
    print(users)
    serializer = UserSerializer(users, many=True)
    return Response({"usuarios": serializer.data})