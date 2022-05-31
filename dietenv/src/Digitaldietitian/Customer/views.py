from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect
from .models import *
from .serializers import *
from rest_framework.parsers import JSONParser,MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,permissions,viewsets
from rest_framework.decorators import api_view,action
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

fs=FileSystemStorage(location='tmp/')

@api_view(['GET', 'POST'])
def userlogin(request):
    """
    User login
    """
    if request.method=='POST':
        username = request.POST['email']
        password = request.POST['password']
        user = login(username=username, password=password)
        if user is not None:
            return redirect('/user/{user.email}')  
        else:
            # Return an 'invalid login' error message.
            ...
    if request.method=='GET':
        return redirect('register')

class UserRegister(generics.GenericAPIView):
    serializer_class=CustomerSerializers
    queryset=Customer.objects.all()
    lookup_field = 'email'

    def get(self, request,pk=None):
        if pk is not None:
            try:
                user = Customer.objects.get(email=pk)
                serializer = CustomerSerializers(user)
            except Exception as e:
                e.with_traceback("User does not exist")
            return Response(serializer.data)
        else:
            users = Customer.objects.all()
            serializer = CustomerSerializers(users, many=True)
            return Response(serializer.data)

    

    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk,format=None):
    """
    Retrieve, update or delete a customer.
    """
    try:
        customer = Customer.objects.get(email=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializers(customer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializers(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FoodViewsets(viewsets.ModelViewSet):
    """
    Food Data
    """
    queryset=FoodData.objects.all()
    serializer_class=FoodSerializer
    @action(detail=False,methods=['POST'])
    def upload_data(request):
        file=request.FILES['file']
        content=file.read()
        file_content=ContentFile(content)
        file_name=fs.save(
            "tmp.csv",file_content
        )
        tmp_file=fs.path(file_name)
        csv_file=open(tmp_file,errors="ignore")
        reader=csv.reader(csv_file)
        next(reader)

        for id_,row in enumerate(reader):
            (Name,Alpha_Carotene,Ash,	Beta_Carotene,	Beta_Cryptoxanthin,	Carbohydrate,	Cholesterol,	Choline,Fiber,
            	Kilocalories,Lutein_and_Zeaxanthin,	Lycopene,Manganese,	Niacin,	Pantothenic_Acid,Protein,	Refuse_Percentage,
                	Retinol	,Riboflavin,Selenium,Sugar_Total,	Thiamin,Water,	Fat_Monosaturated_Fat,	Fat_Polysaturated_Fat,Fat_Saturated_Fat,
                    	Fat_Total_Lipid,	Major_Minerals_Calcium,	Major_Minerals_Copper,	Major_Minerals_Iron,	Major_Minerals_Magnesium,	Major_Minerals_Phosphorus,
                        	Major_Minerals_Potassium,	Major_Minerals_Sodium,	Major_Minerals_Zinc,	Vitamins_Vitamin_A_IU,	Vitamins_Vitamin_A_RAE,
                            	Vitamins_Vitamin_B12,	Vitamins_Vitamin_B6,	Vitamins_Vitamin_C,	Vitamins_Vitamin_E,	Vitamins_Vitamin_K,	Household_Weights_2nd_Household_Weight_Description
            )=row

class RegionView(generics.GenericAPIView):
    serializer_class=RegionSerializer
    queryset=Region.objects.all()
    lookup_field = 'regionName'

    def get(self, request):
            region = Region.objects.values("regionName","regionId")
            serializer = RegionSerializer(region, many=True)
            return Response(serializer.data)

class ZoneView(generics.GenericAPIView):
    serializer_class=ZoneSerializer
    queryset=Zone.objects.all()
    lookup_field = 'zoneName'

    def get(self, request):
        zone = Zone.objects.values('zoneName','zoneId')
        serializer = ZoneSerializer(zone, many=True)
        return Response(serializer.data)

class ExercisingView(generics.GenericAPIView):
    serializer_class=ExerciseSerializer
    queryset=ExercisingRate.objects.all()
    lookup_field = 'ERName'

    def get(self, request):
        exercising = ExercisingRate.objects.values('ERName','ERId')
        serializer =ExerciseSerializer(exercising, many=True)
        return Response(serializer.data)

class DiseaseView(generics.GenericAPIView):
    serializer_class=DiseasesSerializer
    queryset=Diseases.objects.all()
    lookup_field = 'DName'

    def get(self, request):
        disease = Diseases.objects.values('DId','DName')
        serializer =DiseasesSerializer(disease, many=True)
        return Response(serializer.data)