import email
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse

# rest framework imports
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from rest_framework import generics
from urllib import response
from rest_framework.views import APIView


# local imports
from .serializers import *
from .models import *
from insurance.models import *
import uuid

# Create your views here.

# index page api
@api_view(["GET"])
@permission_classes((AllowAny,))
def index(request):
    """
    Index API
    """
    return Response({"message": "Welcome to assessment API service"})


#######################################
# User APIs below
#######################################


class RegistrationAPIView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def Login(request):
    email = request.data['email']
    password = request.data['password']
    user = Customer.objects.filter(email=email).first()

    if user is None:
        AuthenticationFailed.status_code()
        raise AuthenticationFailed('Incorrect authentication credentials.r')
    if not user.check_password(password):
        raise AuthenticationFailed('user is not exist please enter valid user again')

        return response({
            'message': 'success'
            })
        
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
# @permission_classes((AllowAny,))
def Users_list_api(request, format=None):
    """
    Start the new insurenece giving list of all question papers
    """
    if request.method == 'GET':
        user = Customer.objects.all()
        serializer = CustomerSerializer(user, many=True)
        return Response (serializer.data)
        

@api_view(['POST','GET'])
def Education_api_detail(request, format=None):
    """
    POST, Retrieve, update or delete vehicle.
    """
  
    if  request.method == 'POST':
        serializer = EducationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data, status = status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        createExam = Education.objects.all()
        serializer = EducationSerializer(createExam, many = True)
        return Response(serializer.data)

    # elif request.method == 'PUT':
    #     serializer = EducationSerializer(dtata = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     question.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','GET', 'PUT', 'DELETE'])
def ProfessionsubOccupation_Description_api_detail(request, pk, format=None):
    """
    POST, Retrieve, update or delete vehicle.
    """
    try:
        question = ProfessionsubOccupation_DescriptionSerializer.objects.get(pk=pk)
    except ProfessionsubOccupation_DescriptionSerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if  request.method == 'POST':
        serializer = ProfessionsubOccupation_DescriptionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data, status = status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = ProfessionsubOccupation_DescriptionSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfessionsubOccupation_DescriptionSerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST','GET', 'PUT', 'DELETE'])
def InsurenceCategory(request, pk, format=None):
    """
    POST, Retrieve, update or delete vehicle.
    """
    try:
        question = InsurenceCategorySerializer.objects.get(pk=pk)
    except InsurenceCategorySerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if  request.method == 'POST':
        serializer = InsurenceCategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data, status = status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = InsurenceCategorySerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InsurenceCategorySerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','GET', 'PUT', 'DELETE'])
def Profession_api_detail(request, pk, format=None):
    """
    POST, Retrieve, update or delete vehicle.
    """
    try:
        question = ProfessionSerializer.objects.get(pk=pk)
    except ProfessionSerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if  request.method == 'POST':
        serializer = ProfessionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data, status = status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = ProfessionSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfessionSerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','GET', 'PUT', 'DELETE'])
def PersonalProfile_api_detail(request, pk, format=None):
    """
    POST, Retrieve, update or delete vehicle.
    """
    try:
        question = PersonalProfileSerializer.objects.get(pk=pk)
    except PersonalProfileSerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if  request.method == 'POST':
        serializer = PersonalProfileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data, status = status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = PersonalProfileSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonalProfileSerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','GET', 'PUT', 'DELETE'])
def Policy_api_detail(request, pk, format=None):
    """
    POST, Retrieve, update or delete vehicle.
    """
    try:
        question = PolicySerializer.objects.get(pk=pk)
    except PolicySerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if  request.method == 'POST':
        serializer = PolicySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data, status = status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = PolicySerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PolicySerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['POST','GET', 'PUT', 'DELETE'])
def PolicyRecord_api_detail(request, pk, format=None):
    """
    POST, Retrieve, update or delete vehicle.
    """
    try:
        question = PolicyRecordSerializer.objects.get(pk=pk)
    except PolicyRecordSerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if  request.method == 'POST':
        serializer = PolicyRecordSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data, status = status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = PolicyRecordSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PolicyRecordSerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','GET', 'PUT', 'DELETE'])
def VehicleCategory_api_detail(request, pk, format=None):
    """
    POST, Retrieve, update or delete vehicle.
    """
    try:
        question = VehicleCategorySerializer.objects.get(pk=pk)
    except VehicleCategorySerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if  request.method == 'POST':
        serializer = VehicleCategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data, status = status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'GET':
        serializer = VehicleCategorySerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VehicleCategorySerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','GET', 'PUT', 'DELETE'])
def Primium_api_detail(request, pk, format=None):
    """
    POST, Retrieve, update or delete vehicle.
    """
    try:
        question = PrimiumSerializer.objects.get(pk=pk)
    except PrimiumSerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if  request.method == 'POST':
        serializer = PrimiumSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data, status = status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'GET':
        serializer = PrimiumSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PrimiumSerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','GET', 'PUT', 'DELETE'])
def FeedBack_customer_api_detail(request, pk, format=None):
    """
    POST, Retrieve, update or delete vehicle.
    """
    try:
        question = FeedBack_customerSerializer.objects.get(pk=pk)
    except FeedBack_customerSerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if  request.method == 'POST':
        serializer = FeedBack_customerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data, status = status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = FeedBack_customerSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FeedBack_customerSerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','GET', 'PUT', 'DELETE'])
def FeedBack_api_detail(request, pk, format=None):
    """
    POST, Retrieve, update or delete vehicle.
    """
    try:
        question = FeedBackSerializer.objects.get(pk=pk)
    except FeedBackSerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if  request.method == 'POST':
        serializer = FeedBackSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data, status = status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = FeedBackSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FeedBackSerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','GET', 'PUT', 'DELETE'])
def Insured_api_detail(request, pk, format=None):
    """
    POST, Retrieve, update or delete vehicle.
    """
    try:
        question = InsuredSerializer.objects.get(pk=pk)
    except InsuredSerializer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if  request.method == 'POST':
        serializer = InsuredSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data, status = status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        serializer = InsuredSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InsuredSerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST','GET', 'PUT', 'DELETE'])
def CoverIdentification_api_detail(request, pk, format=None):
    """
    POST, Retrieve, update or delete vehicle.
    """
    try:
        question = CoverIdentification.objects.get(pk=pk)
    except CoverIdentification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if  request.method == 'POST':
        serializer = CoverIdentificationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()          
            return Response(serializer.data, status = status.HTTP_201_CREATED)         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'GET':
        serializer = CoverIdentificationSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CoverIdentificationSerializer(dtata = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



