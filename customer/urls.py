from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from customer.views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('register', RegistrationAPIView.as_view(), name='user'),
    path('login/', views.Login, name='login'),


    path('Users_list_api/', views.Users_list_api, name='Users_list_api'),
    path('Education_api/', views.Education_api_detail, name = 'Education_api_detail'),
    path('Education_api_detail/<int:pk>/', views.Education_api_detail, name='Education_api_detail'),
    path('ProfessionsubOccupation/list', views.ProfessionsubOccupation_Description_api_detail, name= 'listProfessionsubOccupation'),
    path('ProfessionsubOccupation/<int:pk>/', views.ProfessionsubOccupation_Description_api_detail, name= 'listProfessionsubOccupationByID'),
    path('InsurenceCategory/list/', views.InsurenceCategory, name='InsurenceCategory'),
    path('InsurenceCategory/<int:pk>',views.Profession_api_detail, name = 'InsurenceCategoryBYid'),
    path('PersonalProfile/add/list/', views.PersonalProfile_api_detail, name='list_PersonalProfile'),
    path('Policy/api/', views.Policy_api_detail, name='Policy'),
    path('Policy/details/<int:pk>', views.Policy_api_detail, name = 'Policybyid'),

    path('PolicyRecord/', views.PolicyRecord_api_detail, name='PolicyRecord_list_api'),
    path('PolicyRecord_api_detail/<int:pk>/', views.PolicyRecord_api_detail, name='Education_api_detail'),
    path('VehicleCategory/', views.VehicleCategory_api_detail, name = 'VehicleCategory'),
    path('VehicleCategory_api_detail/<int:pk>/', views.VehicleCategory_api_detail, name='Education_api_detail'),
    path('Primium/list', views.Primium_api_detail, name= 'Primium'),
    path('Primium/<int:pk>/', views.Primium_api_detail, name= 'Primiumbyid'),
    path('FeedBack_customer/list/', views.FeedBack_customer_api_detail, name='FeedBack_customer'),
    path('FeedBack_customer/<int:pk>',views.FeedBack_customer_api_detail, name = 'FeedBack_customer'),
    path('FeedBack/add/list/', views.FeedBack_api_detail, name='FeedBack'),
    path('FeedBack/details/<int:pk>', views.FeedBack_api_detail, name = 'FeedBackbyid'),
    path('Insured_/api/', views.Insured_api_detail, name='Insured_'),
    path('Insured_/details/<int:pk>', views.Insured_api_detail, name = 'Insured'),
    path('CoverIdentification_/api/', views.CoverIdentification_api_detail, name='CoverIdentification'),
    path('CoverIdentification/details/<int:pk>', views.CoverIdentification_api_detail, name = 'CoverIdentificationbyid'),

]