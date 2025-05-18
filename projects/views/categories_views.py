from rest_framework import status
from rest_framework.views import APIView
from ..serializers.categories_serializer import CategoriesSerializer, CategoriesInfoSerializer
from ..models import Categories, CategoriesInfo
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

class GetCategoriesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CategoriesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Creado exitosamente"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)
    
class GetTeamsCategoriesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id_category=None):
        if id_category is not None:
            try:
                category = CategoriesInfo.objects.filter(id_category=id_category)
                serializer = CategoriesInfoSerializer(category, many=True)
                return Response(serializer.data)
            except CategoriesInfo.DoesNotExist:
                return Response({'detail': 'Categoría no encontrada.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            category = CategoriesInfo.objects.all()
            serializer = CategoriesInfoSerializer(category, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        serializer = CategoriesInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Creado exitosamente"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)