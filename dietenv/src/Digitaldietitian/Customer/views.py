from datetime import datetime
from django.shortcuts import redirect
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage
from .CustomerAuthentication import loginme
from dietitian.models import FoodData
from django.db.models import Q

fs=FileSystemStorage(location='tmp/')

def days_between(d1, d2):
    d1 = datetime.strptime(str(d1), "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

@api_view(['GET', 'POST'])
def userlogin(request):
    """
    User login
    """
    if request.method=='POST':
        username = request.data.get('email')
        password = request.data.get('password')
        user = loginme(username,password)
        if user is not None:
            serializers=CustomerSerializers(user,many=False)
            return Response(serializers.data)  
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

class FoodView(generics.GenericAPIView):
    serializer_class=MealAssignedSerializer
    queryset=MealAssigned.objects.all()
    # lookup_field='name'
    def get(self,request):
        meal=MealAssigned.objects.all()
        serializer=MealAssignedSerializer(meal, many=True)
        return Response(serializer.data)
    def get(self,request,pk):
        lastlogin = Customer.objects.values('lastlogin').get(email=pk)
        k=lastlogin
        # using a timedelta avoids having to know about length of months etc:
        now = datetime.today().date()
        # returns a timedelta object:
        difference = days_between(now,k['lastlogin'])
        if  difference>0:
            customer=Customer.objects.select_related('healthStatus').get(email=pk)
            customer.lastlogin=now
            customer.save()

            if customer.healthStatus_id==1:
                morning=FoodData.objects.values('name').filter(Q(carbohydrate__lte=30) & Q(mineralsCalcium__lte=900)& Q(vitamin_B12__gt=0)& Q(vitamin_B6__gt=0)& Q(vitamin_C__gt=0)& Q(vitamin_E__gt=0) & Q(vitamin_K__gt=0)& Q(vitamin_A_IU__gt=0)& Q(vitamin_A_RAE__gt=0),mealTime__mtName='Kifungua kinywa').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Kifungua kinywa')
                for food in morning:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=datetime.today(),mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()
                noon=FoodData.objects.values('name').filter(Q(carbohydrate__lte=30) & Q(mineralsCalcium__lte=900)& Q(vitamin_B12__gt=0)& Q(vitamin_B6__gt=0)& Q(vitamin_C__gt=0)& Q(vitamin_E__gt=0) & Q(vitamin_K__gt=0)& Q(vitamin_A_IU__gt=0)& Q(vitamin_A_RAE__gt=0),mealTime__mtName='Chakula cha mchana').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Chakula cha mchana')
                for food in noon:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=datetime.today(),mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()
                night=FoodData.objects.values('name').filter(Q(carbohydrate__lte=30) & Q(mineralsCalcium__lte=900)& Q(vitamin_B12__gt=0)& Q(vitamin_B6__gt=0)& Q(vitamin_C__gt=0)& Q(vitamin_E__gt=0) & Q(vitamin_K__gt=0)& Q(vitamin_A_IU__gt=0)& Q(vitamin_A_RAE__gt=0),mealTime__mtName='Chakula cha Usiku').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Chakula cha Usiku')
                for food in night:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=datetime.today(),mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()

            elif customer.healthStatus_id==2:
                morning=FoodData.objects.values('name').filter(carbohydrate__lte=30,mealTime__mtName='Kifungua kinywa').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Kifungua kinywa')
                for food in morning:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=datetime.today(),mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()
                noon=FoodData.objects.values('name').filter(carbohydrate__lte=30,mealTime__mtName='Chakula cha mchana').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Chakula cha mchana')
                for food in noon:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=datetime.today(),mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()
                night=FoodData.objects.values('name').filter(carbohydrate__lte=30,mealTime__mtName='Chakula cha Usiku').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Chakula cha Usiku')
                for food in night:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=datetime.today(),mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()

            elif customer.healthStatus_id==3:
                morning=FoodData.objects.values('name').filter(vitamin_A_IU__lte=900,mealTime__mtName='Kifungua kinywa').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Kifungua kinywa')
                for food in morning:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=datetime.today(),mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()
                noon=FoodData.objects.values('name').filter(vitamin_A_IU__lte=900,mealTime__mtName='Chakula cha mchana').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Chakula cha mchana')
                for food in noon:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=datetime.today(),mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()
                night=FoodData.objects.values('name').filter(vitamin_A_IU__lte=900,mealTime__mtName='Chakula cha Usiku').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Chakula cha Usiku')
                for food in night:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=datetime.today(),mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()

            elif customer.healthStatus_id==4:
                morning=FoodData.objects.values('name').filter(mealTime__mtName='Kifungua kinywa').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Kifungua kinywa')
                for food in morning:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=now,mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()
                noon=FoodData.objects.values('name').filter(mealTime__mtName='Chakula cha mchana').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Chakula cha mchana')
                for food in noon:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=now,mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()
                night=FoodData.objects.values('name').filter(mealTime__mtName='Chakula cha Usiku').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Chakula cha Usiku')
                for food in night:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=now,mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()

            elif customer.healthStatus_id==5:
                morning=FoodData.objects.values('name').filter( Q(cholesterol__lte=300)& (Q(carbohydrate__lte=30)|Q(vitamin_A_IU__gte=900)) & Q(mealTime__mtName='Kifungua kinywa')).order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Kifungua kinywa')
                for food in morning:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=datetime.today(),mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()
                noon=FoodData.objects.values('name').filter(Q(cholesterol__lte=300)& (Q(carbohydrate__lte=30)|Q(vitamin_A_IU__gte=900)),mealTime__mtName='Chakula cha mchana').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Chakula cha mchana')
                for food in noon:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=datetime.today(),mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()
                night=FoodData.objects.values('name').filter(Q(cholesterol__lte=300)& (Q(carbohydrate__lte=30)|Q(vitamin_A_IU__gte=900)),mealTime__mtName='Chakula cha Usiku').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Chakula cha Usiku')
                for food in night:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=datetime.today(),mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()

            elif customer.healthStatus_id==6:
                morning=FoodData.objects.values('name').filter(protein__gt=0,carbohydrate__lte=30,water__gte=75,mealTime__mtName='Kifungua kinywa').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Kifungua kinywa')
                for food in morning:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=now,mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()
                noon=FoodData.objects.values('name').filter(protein__gt=0,carbohydrate__lte=30,water__gte=75,mealTime__mtName='Chakula cha mchana').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Chakula cha mchana')
                for food in noon:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=now,mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()
                night=FoodData.objects.values('name').filter(protein__gt=0,carbohydrate__lte=30,water__gte=75,mealTime__mtName='Chakula cha Usiku').order_by('?')[:3]
                mealtime=MealtimeName.objects.get(mtName='Chakula cha Usiku')
                for food in night:
                    foodobj=FoodData.objects.get(name=food['name'])
                    mealassigned=MealAssigned.objects.create(dateofentry=now,mealTime=mealtime,customer=customer,food=foodobj)
                    mealassigned.save()

            else:
                return Response()
            mealassigned=MealAssigned.objects.filter(customer_id=pk,dateofentry=now)[:9]
            serializer=MealAssignedSerializer(mealassigned, many=True)
            return Response(serializer.data)

        else:

            mealassigned=MealAssigned.objects.filter(customer_id=pk,dateofentry=k['lastlogin'])[:9]
            serializer=MealAssignedSerializer(mealassigned, many=True)
            return Response(serializer.data)

class Food_detailsView(generics.GenericAPIView):
    serializer_class=FoodSerializer
    queryset=FoodData.objects.all()
    def get(self,request):
        fooddetails=FoodData.objects.all()
        serializer=FoodSerializer(fooddetails,many=True)
        return Response(serializer.data)
    def get(self,request,pk=None):
        fooddetails=FoodData.objects.get(name=pk)
        serializer=FoodSerializer(fooddetails)
        return Response(serializer.data)


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