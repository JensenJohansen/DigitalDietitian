from django.contrib.auth import authenticate, login
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

def registration(request):
    pass

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

class UserRegister(generics.GenericAPIView):
    serializer_class=CustomerSerializers
    queryset=Customer.objects.all()

    def get(self, request):
        users = Customer.objects.all()
        serializer = CustomerSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        
        jdata= JSONRenderer().render(request.data)
        stream = io.BytesIO(jdata)
        data = JSONParser().parse(stream)
        serializer = CustomerSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)