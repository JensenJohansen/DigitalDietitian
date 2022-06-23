from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import decorators, status,generics,permissions,viewsets
from Customer.serializers import *
from .models import *
from rest_framework.decorators import api_view

# Create your views here.

class DataViewApi(generics.GenericAPIView):
    def get(self,request,instance=None):
        """
            retrieving data for specific 
        """
        if instance == "region":
            try:
                region = Region.objects.values('regionName')
            except region.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            if request.method == 'GET':
                region = Region.objects.values('regionName')
                serializer = RegionSerializer(region)
                return Response(serializer.data)

        elif instance == "exercising" and request.method == 'GET':
            exercising = ExercisingRate.objects.values('ERName')
            serializer = ExerciseSerializer(exercising)
            return Response(serializer.data)

        elif instance == "diseases" and request.method == 'GET':
            diseases = Diseases.objects.values('DName')
            serializer = DiseasesSerializer(diseases)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def region_detail(request, pk,format=None):
    """
    Retrieve, update or delete a region
    """
    try:
        region = Region.objects.get(regionId=pk)
    except region.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegionSerializer(region)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        region.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)