from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from customer.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Shaka.com API",
      default_version='v1',
      description="We have created an insurance retails platform called kiza which helps people to get e quotation and purchase insurance from their mobile or laptop devices. Those who don’t have computer literacy can approach anyone with those skills or public secretary service providers(irembo’s agents, printing services, RRA declaration offices,...)to help them push insurance at any time.",
      contact=openapi.Contact(email="sentongoalbert12@gmail.com"),
      
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

app_name = 'customer'

urlpatterns = [
    path('message', views.index, name='index'),
    path('register', RegistrationAPIView.as_view(), name='user'),
    path('login/', views.Login, name='login'),
    path('Users_list_api', views.Users_list_api, name='Users_list_api'),
    path('Education_api', views.Education_api, name = 'Education_api_detail'),
    path('Education_api_detail/<int:pk>', views.Education_api_detail, name='Education_api_detail'),
    path('ProfessionsubOccupation/list', views.ProfessionsubOccupation_Description_api, name= 'listProfessionsubOccupation'),
    path('ProfessionsubOccupation/<int:pk>', views.ProfessionsubOccupation_detail, name= 'listProfessionsubOccupationByID'),
    path('InsurenceCategory/list', views.InsurenceCategor, name='InsurenceCategory'),
    path('InsurenceCategorydetails/<int:pk>',views.InsurenceCategory_detail, name = 'InsurenceCategoryBYid'),
    path('PersonalProfile/add/list', views.PersonalProfil, name='list_PersonalProfile'),
    path('PersonalProfile_api_detail/<int:pk>',views.PersonalProfile_api_detail, name = 'PersonalProfile_api_detail'),
    path('Policy/api/', views.Policy_api, name='Policy'),
    path('Policy/details/<int:pk>', views.Policy_api_detail, name = 'Policybyid'),

    path('PolicyRecord', views.PolicyRecord_api, name='PolicyRecord_list_api'),
    path('PolicyRecord_api_detail/<int:pk>', views.PolicyRecord_api_detail, name='Education_api_detail'),
    path('VehicleCategory/', views.VehicleCategory_api, name = 'VehicleCategory'),
    path('VehicleCategory_api_detail/<int:pk>', views.VehicleCategory_api_detail, name='Education_api_detail'),
    path('Primium/list', views.Primium_api, name= 'Primium'),
    path('Primium/<int:pk>', views.Primium_api_detail, name= 'Primiumbyid'),
    path('FeedBack_customer/list', views.FeedBack_customer_api, name='FeedBack_customer'),
    path('FeedBack_customer/<int:pk>',views.FeedBack_customer_api_detail, name = 'FeedBack_customer'),
    path('FeedBack/add/list/', views.FeedBack_api, name='FeedBack'),
    path('FeedBack/details/<int:pk>', views.FeedBack_api_detail, name = 'FeedBackbyid'),
    path('Insured_/api', views.Insured_api, name='Insured_'),
    path('Insured_/details/<int:pk>', views.Insured_api_detail, name = 'Insured'),
    path('CoverIdentification_/api', views.CoverIdentification_api, name='CoverIdentification'),
    path('CoverIdentification/details/<int:pk>', views.CoverIdentification_api_detail, name = 'CoverIdentificationbyid'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]

