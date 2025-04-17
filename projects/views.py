from rest_framework import viewsets,permissions, status
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def login(request):
    print(request.data['data'])
    user = get_object_or_404(User, email=request.data['data']['email'])

    if not user.check_password(request.data['data']['password']):
        return Response({"error": "Contraseña incorrecta"}, status = status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def getUsers(request):
    users = User.objects.all()
    print(users)
    serializer = UserSerializer(users, many=True)
    return Response({"usuarios": serializer.data})