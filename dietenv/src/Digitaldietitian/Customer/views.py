from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,permissions,viewsets
from rest_framework.decorators import api_view


def registration(request):
    pass


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