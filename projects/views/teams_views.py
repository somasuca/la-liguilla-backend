from rest_framework import status
from rest_framework.views import APIView
from ..serializers.teams_serializer import TeamsSerializer
from ..models import Teams
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

# @api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def createTeam(request):
#     serializer = TeamsSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Creado exitosamente"}, status=status.HTTP_201_CREATED)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def getTeams(self):
#     teams = Teams.objects.all()
#     serializer = TeamsSerializer(teams, many=True)
#     return Response(serializer.data)

class GetTeamsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        teams = Teams.objects.all()
        serializer = TeamsSerializer(teams, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeamsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Creado exitosamente"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

