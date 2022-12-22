

from rest_framework import serializers
from logging import raiseExceptions
from .models import *
from customer.models import *
from .models import User
from rest_framework import serializers,status
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password
from insurance.models import *



class CustomerSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=40,allow_blank=True)
    email = serializers.EmailField(max_length=80,allow_blank=False)
    mobile = serializers.CharField(allow_null=False,allow_blank=False)
    password=serializers.CharField(allow_blank=False,write_only=True)
    class Meta:
        model=Customer
        fields=['id','username', 'email', 'mobile','password']

    def validate(self,attrs):
        email=Customer.objects.filter(username=attrs.get('username')).exists()

        if email:
            raise ValidationError(detail="User with email exists",code=status.HTTP_403_FORBIDDEN)

        username=Customer.objects.filter(username=attrs.get('username')).exists()

        if username:
            raise ValidationError(detail="User with username exists",code=status.HTTP_403_FORBIDDEN)

        return super().validate(attrs)


    def create(self,validated_data):
        new_user=Customer(**validated_data)

        new_user.password=make_password(validated_data.get('password'))

        new_user.save()

        return new_user




class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class ProvinceSerializer(serializers.ModelSerializer):
    Country = serializers.StringRelatedField()
    class Meta:
        model = Province
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    province = serializers.StringRelatedField()
    Country = serializers.StringRelatedField()
    class Meta:
        model = District
        fields = '__all__'

class SectorSerializer(serializers.ModelSerializer):
    province = serializers.StringRelatedField()
    district = serializers.StringRelatedField()
    Country = serializers.StringRelatedField()
    class Meta:
        model = Sector
        fields = '__all__'

class CellSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    profession = serializers.StringRelatedField()
    education = serializers.StringRelatedField()
    class Meta:
        model = Cell
        fields = '__all__'

class VillageSerializer(serializers.ModelSerializer):
    province = serializers.StringRelatedField()
    district = serializers.StringRelatedField()
    sector = serializers.StringRelatedField()
    Country = serializers.StringRelatedField()
    class Meta:
        model = Village
        fields = '__all__'
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ProfessionsubOccupation_DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = '__all__'


class InsurenceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsurenceCategory
        fields = '__all__'

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OccupationSub
        fields = '__all__'

class PersonalProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    profession = serializers.StringRelatedField()
    education = serializers.StringRelatedField()
    class Meta:
        model = PersonalProfile
        fields = '__all__'
class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'
class PolicyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyRecord
        fields = '__all__'
class VehicleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCategory
        fields = '__all__'

class CoverIdentificationSerializer(serializers.ModelSerializer):
    vehicle_usage = serializers.StringRelatedField()
    vehicleowner = serializers.StringRelatedField()
     
    class Meta:
        model = CoverIdentification
        fields = '__all__'

class PrimiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Primium
        fields = '__all__'

class InsuredSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    class Meta:
        model = Insured
        fields = '__all__'

class FeedBack_customerSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    class Meta:
        model = Insured
        fields = '__all__'

class FeedBackSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    class Meta:
        model = Insured
        fields = '__all__'