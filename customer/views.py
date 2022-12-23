# import email
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt
# from django.http.response import HttpResponse

# # rest framework imports
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
# from rest_framework.status import (
#     HTTP_400_BAD_REQUEST,
#     HTTP_404_NOT_FOUND,
#     HTTP_200_OK,
#     HTTP_201_CREATED,
#     HTTP_204_NO_CONTENT
# )
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
# from rest_framework import viewsets
# from rest_framework.generics import ListAPIView, CreateAPIView
# from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
# from rest_framework import generics
# from urllib import response
# from rest_framework.views import APIView
# from drf_yasg.utils import swagger_auto_schema


# # local imports
# from .serializers import *
# from .models import *
# from insurance.models import *
# import uuid

# # Create your views here.

# # index page api
# @api_view(["GET"])
# @permission_classes((AllowAny,))
# def index(request):
#     """
#     Index API
#     """
#     return Response({"message": "Welcome to assessment API service"})


# #######################################
# # User APIs below
# #######################################


# class RegistrationAPIView(generics.ListCreateAPIView):
   
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
    
#     def post(self, request):
#         serializer = self.get_serializer(data = request.data)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response({
#                 "RequestId": str(uuid.uuid4()),
#                 "Message": "User created successfully",
                
#                 "User": serializer.data}, status=status.HTTP_201_CREATED
#                 )
        
#         return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def Login(request):
#     email = request.data['email']
#     password = request.data['password']
#     user = Customer.objects.filter(email=email).first()

#     if user is None:
#         AuthenticationFailed.status_code()
#         raise AuthenticationFailed('Incorrect authentication credentials.r')
#     if not user.check_password(password):
#         raise AuthenticationFailed('user is not exist please enter valid user again')

#         return response({
#             'message': 'success'
#             })
        
# @api_view(['GET'])
# @permission_classes((IsAuthenticated,))
# def Users_list_api(request, format=None):
#     """
#     Start the new insurenece giving list of all question papers
#     """
#     if request.method == 'GET':
#         user = Customer.objects.all()
#         serializer = CustomerSerializer(user, many=True)
#         return Response (serializer.data)
        

# @api_view(['POST','GET'])
# @swagger_auto_schema(operation_summary="Create an Education and store in database")
# @permission_classes((IsAuthenticated,))
# def Education_api(request, format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
#     if  request.method == 'POST':
#         serializer = EducationSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()          
#             return Response({
#                 "RequestId": str(uuid.uuid4()),
#                 "Message": "Education created successfully",
                
#                 "Education": serializer.data}, status=status.HTTP_201_CREATED
#                 )        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'GET':
#         createExam = Education.objects.all()
#         serializer = EducationSerializer(createExam, many = True)
#         return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def Education_api_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code Exam.
#     """
#     try:
#         education = Education.objects.get(pk=pk)
#     except Education.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = EducationSerializer(education)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = EducationSerializer(education, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         education.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['POST','GET'])
# @permission_classes((IsAuthenticated,))
# def ProfessionsubOccupation_Description_api(request,format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """

#     if  request.method == 'POST':
#         serializer = ProfessionsubOccupation_DescriptionSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()          
#             return Response(serializer.data, status = status.HTTP_201_CREATED)         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'GET':
#         createExam = ProfessionsubOccupation_Description.objects.all()
#         serializer = ProfessionsubOccupation_DescriptionSerializer(createExam, many = True)
#         return Response(serializer.data)

    

# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def ProfessionsubOccupation_detail(request, pk, format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
#     try:
#         question = ProfessionsubOccupation_DescriptionSerializer.objects.get(pk=pk)
#     except ProfessionsubOccupation_DescriptionSerializer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProfessionsubOccupation_DescriptionSerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ProfessionsubOccupation_DescriptionSerializer(dtata = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['POST','GET'])
# @permission_classes((IsAuthenticated,))
# def InsurenceCategor(request,format=None):
#     """
#     POST,Retrieve, update or delete vehicle.
#     """
#     if  request.method == 'POST':
#         serializer = InsurenceCategorySerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()          
#             return Response(serializer.data, status = status.HTTP_201_CREATED)         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'GET':
#         createExam =InsurenceCategory.objects.all()
#         serializer = InsurenceCategorySerializer(createExam, many = True)
#         return Response(serializer.data)

    

# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def InsurenceCategory_detail(request, pk, format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
#     try:
#         question = ProfessionsubOccupation_DescriptionSerializer.objects.get(pk=pk)
#     except ProfessionsubOccupation_DescriptionSerializer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProfessionsubOccupation_DescriptionSerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ProfessionsubOccupation_DescriptionSerializer(dtata = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# @api_view(['POST','GET'])
# @permission_classes((IsAuthenticated,))
# def PersonalProfil(request,format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
 
#     if  request.method == 'POST':
#         serializer = PersonalProfileSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()          
#             return Response(serializer.data, status = status.HTTP_201_CREATED)         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'GET':
#         createExam = PersonalProfile.objects.all()
#         serializer = PersonalProfileSerializer(createExam, many = True)
#         return Response(serializer.data)

    
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def PersonalProfile_api_detail(request, pk, format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
#     try:
#         question = PersonalProfileSerializer.objects.get(pk=pk)
#     except PersonalProfileSerializer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


#     if request.method == 'GET':
#         serializer = PersonalProfileSerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PersonalProfileSerializer(dtata = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST','GET'])
# @permission_classes((IsAuthenticated,))
# def Policy_api(request,format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
#     if  request.method == 'POST':
#         serializer = PolicySerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()          
#             return Response(serializer.data, status = status.HTTP_201_CREATED)         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'GET':
#         createExam = Policy.objects.all()
#         serializer = PolicySerializer(createExam, many = True)
#         return Response(serializer.data)

   


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def Policy_api_detail(request, pk, format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
#     try:
#         question = PolicySerializer.objects.get(pk=pk)
#     except PolicySerializer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PolicySerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PolicySerializer(dtata = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST','GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def PolicyRecord_api(request, format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
  
#     if  request.method == 'POST':
#         serializer = PolicyRecordSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()          
#             return Response(serializer.data, status = status.HTTP_201_CREATED)         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'GET':
#         createExam = PolicyRecord.objects.all()
#         serializer = PolicyRecordSerializer(createExam, many = True)
#         return Response(serializer.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def PolicyRecord_api_detail(request, pk, format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
#     try:
#         question = PolicyRecordSerializer.objects.get(pk=pk)
#     except PolicyRecordSerializer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PolicyRecordSerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PolicyRecordSerializer(dtata = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['POST','GET'])
# @permission_classes((IsAuthenticated,))
# def VehicleCategory_api(request,format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
#     if  request.method == 'POST':
#         serializer = VehicleCategorySerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()          
#             return Response(serializer.data, status = status.HTTP_201_CREATED)         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     elif request.method == 'GET':
#         createExam = VehicleCategory.objects.all()
#         serializer = VehicleCategorySerializer(createExam, many = True)
#         return Response(serializer.data)

   
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def VehicleCategory_api_detail(request, pk, format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
#     try:
#         question = VehicleCategorySerializer.objects.get(pk=pk)
#     except VehicleCategorySerializer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = VehicleCategorySerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = VehicleCategorySerializer(dtata = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['POST','GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def Primium_api(request,format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
  

#     if  request.method == 'POST':
#         serializer = PrimiumSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()          
#             return Response(serializer.data, status = status.HTTP_201_CREATED)         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'GET':
#         createExam = Primium.objects.all()
#         serializer = PrimiumSerializer(createExam, many = True)
#         return Response(serializer.data)



# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def Primium_api_detail(request, pk, format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
#     try:
#         question = PrimiumSerializer.objects.get(pk=pk)
#     except PrimiumSerializer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PrimiumSerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = PrimiumSerializer(dtata = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)  

# @api_view(['POST','GET'])
# @permission_classes((IsAuthenticated,))
# def FeedBack_customer_api(request,format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """


#     if  request.method == 'POST':
#         serializer = FeedBack_customerSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()          
#             return Response(serializer.data, status = status.HTTP_201_CREATED)         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'GET':
#         createExam = Primium.objects.all()
#         serializer = PrimiumSerializer(createExam, many = True)
#         return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def FeedBack_customer_api_detail(request, pk, format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
#     try:
#         question = FeedBack_customerSerializer.objects.get(pk=pk)
#     except FeedBack_customerSerializer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


#     if request.method == 'GET':
#         serializer = FeedBack_customerSerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = FeedBack_customerSerializer(dtata = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['POST','GET'])
# @permission_classes((IsAuthenticated,))
# def Insured_api(request, format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """

#     if  request.method == 'POST':
#         serializer = InsuredSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()          
#             return Response(serializer.data, status = status.HTTP_201_CREATED)         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'GET':
#         createExam = Insured.objects.all()
#         serializer = InsuredSerializer(createExam, many = True)
#         return Response(serializer.data)

     
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def Insured_api_detail(request, pk, format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
#     try:
#         question = InsuredSerializer.objects.get(pk=pk)
#     except InsuredSerializer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


#     if request.method == 'GET':
#         serializer = InsuredSerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = InsuredSerializer(dtata = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['POST','GET'])
# @permission_classes((IsAuthenticated,))
# def FeedBack_api(request,format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """

#     if  request.method == 'POST':
#         serializer = FeedBackSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()          
#             return Response(serializer.data, status = status.HTTP_201_CREATED)         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'GET':
#         createExam = FeedBack.objects.all()
#         serializer = FeedBackSerializer(createExam, many = True)
#         return Response(serializer.data)

    
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def FeedBack_api_detail(request, pk, format=None):
#     """
#     POST, Retrieve, update or delete vehicle.
#     """
#     try:
#         question = FeedBackSerializer.objects.get(pk=pk)
#     except FeedBackSerializer.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = FeedBackSerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = FeedBackSerializer(dtata = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['POST','GET'])
# @permission_classes((IsAuthenticated,))
# def CoverIdentification_api(request, format=None):

#     if  request.method == 'POST':
#         serializer = CoverIdentificationSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()          
#             return Response(serializer.data, status = status.HTTP_201_CREATED)         
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     elif request.method == 'GET':
#         createExam = CoverIdentification.objects.all()
#         serializer = CoverIdentificationSerializer(createExam, many = True)
#         return Response(serializer.data)

   

# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((IsAuthenticated,))
# def CoverIdentification_api_detail(request, pk, format=None):
  
#     try:
#         question = CoverIdentification.objects.get(pk=pk)
#     except CoverIdentification.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CoverIdentificationSerializer(question)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CoverIdentificationSerializer(dtata = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




