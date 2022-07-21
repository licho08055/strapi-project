from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404



from .models import Planet,Character
from .serializers import PlanetSerializer,CharacterSerializer
 



@api_view(['GET', 'POST'])
def CharacterListCreateView(request):
    if request.method == 'GET':
        charac = Character.objects.all()
        serializer = CharacterSerializer(charac, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def CharacterDetailUpdateDeleteView(request, id):
    if request.method == 'GET':
        try:
            lister = Character.objects.get(id=id)
        except Character.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = CharacterSerializer(lister)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        lis = get_object_or_404(Character, id=id)
        serializer = CharacterSerializer(lis, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
    
    elif request.method == 'DELETE':
        object_delete = get_object_or_404(Character, id=id)
        object_delete.delete()
        return Response({'msg':'Character deleted!'})
        
            
    
        
        
@api_view(['GET', 'POST'])
def PlanetListCreateView(request):
    if request.method == 'GET':
        list_object = Planet.objects.all()
        serializer = PlanetSerializer(list_object, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PlanetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['GET', 'PUT', 'DELETE'])
def DetailUpdateDeleteView(request, id):
    try:
        detail_object = Planet.objects.get(id=id)
    except Planet.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = PlanetSerializer(detail_object)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PlanetSerializer(detail_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    elif request.method == 'DELETE':
         detail_object.delete()
         return Response({'msg':'Deleted!'})