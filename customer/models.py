from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.timezone import now
from django.utils import timezone
from lib.national_id import NationalID
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError



class Country(models.Model):
    countryname = models.CharField(max_length=80, blank=False,null=False)

    def __str__(self) -> str:
        return self.countryname 

class Province(models.Model):
    Provincename = models.CharField(max_length=80, blank=False,null=False)
    Country = models.ForeignKey(Country,max_length=2, on_delete=models.PROTECT, blank=False,null=False)
    def __str__(self) -> str:
        return self.Provincename   
class District(models.Model):
    districtname = models.CharField(max_length=80, blank=False,null=False)  
    province = models.ForeignKey(Province,max_length=4, on_delete=models.PROTECT, blank=False,null=False)
    Country = models.ForeignKey(Country, on_delete=models.PROTECT,max_length=4, blank=False,null=False)
    
    def __str__(self) -> str:
        return self.districtname 
class Sector(models.Model):
    sectorname = models.CharField(max_length=255, blank=False,null=False)
    district = models.ForeignKey(District, on_delete=models.PROTECT, blank=False,null=False)
    province = models.ForeignKey(Province,max_length=4, on_delete=models.PROTECT, blank=False,null=False)

    def __str__(self) -> str:
        return self.sectorname 

   
class Cell(models.Model):
    cellname = models.CharField(max_length=255, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT, blank=True,null=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, blank=True,null=True)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, blank=True,null=True)
    Country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True,null=True)

    def __str__(self) -> str:
        return self.cellname 

class Village(models.Model):
    villagename = models.CharField(max_length=255, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT, blank=True,null=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, blank=True,null=True)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, blank=True,null=True)
    cell = models.ForeignKey(Cell, on_delete=models.PROTECT, blank=True,null=True)
    Country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True,null=True)

    def __str__(self) -> str:
        return self.villagename 


STATUS = (('Corporate Custome','Corporate Custome'),('Individual Customer','Individual Customer'))
class PoliceHolder(models.Model):
    
    status = models.CharField(max_length=10,blank=False, null=False, choices=STATUS)
    LE_Book = models.CharField(max_length=3,blank=True,default='AO1', null=False)
    Customer_ID = models.CharField(max_length=14,blank=False, null=False, unique=True)
    Salutation = models.ForeignKey(Salutation,on_delete=models.PROTECT, max_length=10, blank=False, null=False)
    National_ID_Type = models.CharField(National_ID_Type,on_delete=models.PROTECT, max_length=4,blank=False,null=False)
    National_ID_Number = models.CharField(max_length=16, blank=False,null=False, unique=True)
    Customer_Name = models.CharField(max_length=80, blank=False, null=False)
    Surname = models.CharField(max_length=80, blank=False, null=False)
    Forename_1 = models.CharField(max_length=80,blank=False, null=False)
    Forename_2 = models.CharField(max_length=80,blank=True, null=False)
    Customer_Acronym = models.CharField(max_length=80, blank=False,null=False)
    Vision_OUC = models.CharField(max_length=10,blank=True, null=False)
    Vision_SBU = models.ForeignKey(Vision_SBU,on_delete=models.PROTECT, max_length=10, blank=False, null=False)
    Customer_Open_Date =  models.DateTimeField(blank=True, null=True)
    Customer_Gender = models.ForeignKey(Customer_Gender,on_delete=models.PROTECT, max_length=10,blank=False, null=False)
    Date_of_Birth = models.DateTimeField(blank=False, null=False)
    Place_of_Birth =  models.ForeignKey(Place_of_Birth,on_delete=models.PROTECT, max_length=80, blank=False, null=False)
    Marital_Status = models.ForeignKey(Marital_Status,on_delete=models.PROTECT,max_length=10,blank=False, null=False)
    Spouse_Name = models.CharField(max_length=80, blank=False, null=False)
    Social_Economic_Class = models.ForeignKey(Social_Economic_Class,on_delete=models.PROTECT,max_length=4,blank=True, null=True)
    Next_of_kin_Name = models.CharField(max_length=80,blank=True, null=True)
    Next_of_kin_ID_Type = models.ForeignKey(Next_of_kin_ID_Type,on_delete=models.PROTECT,max_length=4,blank=True, null=True)
    Next_of_kin_ID_Number = models.CharField(max_length=20, blank=True,null=True)
    Next_of_kin_Telephone = models.CharField(max_length=20, blank=True,null=True)
    Next_of_kin_Email_ID = models.EmailField(max_length=40, blank=True,null=True)
    Number_Of_Dependants = models.CharField(max_length=3, blank=False,null=False)
    Nationality = models.ForeignKey(Nationality, on_delete=models.PROTECT, blank=False,null=False)
    Residence = models.ForeignKey(Residence, on_delete=models.PROTECT, blank=False,null=False)
    Comm_Address_2 =  models.CharField(max_length=100, blank=True, null=True)
    Comm_Village = models.ForeignKey(Comm_Village,on_delete=models.PROTECT, max_length=10,blank=False, null=False)
    Comm_Country = models.ForeignKey(Comm_Country,on_delete=models.PROTECT, max_length=2,blank=False, null=False)
    Comm_Residence_Type = models.ForeignKey(Comm_Residence_Type,on_delete=models.PROTECT, max_length=1, blank=False, null=False)
    Perm_Address_1 = models.CharField(max_length=100, blank=False, null=False)
    Perm_Address_2 = models.CharField(max_length=100, blank=True, null=True)
    Perm_Village = models.ForeignKey(Perm_Village,on_delete=models.PROTECT,max_length=10, blank=True, null=True)
    Perm_Country = models.ForeignKey(Perm_Country,on_delete=models.PROTECT, max_length=2, blank=False, null=False) 
    Email_ID = models.EmailField(max_length=100, blank=False, null=False) 
    Work_Telephone = models.PhoneNumberField(max_length=20, blank=False, null=False)
    Home_Telephone = models.PhoneNumberField(max_length=20, blank=False, null=False)
    Fax_Number_1 = models.PhoneNumberField(max_length=20, blank=True, null=True)
    Fax_Number_2 = models.PhoneNumberField(max_length=20, blank=True, null=True)
    Education = models.ForeignKey(Education, on_delete=models.CASCADE, max_length=4,blank=False,null=True)
    Customer_TIN = models.CharField(max_length=10,blank=True, null=True)
    NAICS_Code = models.ForeignKey(NAICS_Code,on_delete=models.CASCADE,blank=False,null=False, max_length=6)
    Economic_Sub_Sector_Code_ISIC = models.ForeignKey(Economic_Sub_Sector_Code_ISIC, on_delete=models.CASCADE, max_length=10,blank=False,null=False)
    Related_Party = models.ForeignKey(Related_Party,max_length=10, on_delete=models.CASCADE,blank=False,null=False)
    Relationship_Type = models.ForeignKey(Relationship_Type,max_length=4, on_delete=models.CASCADE,blank=False,null=False)
    Related_Party_Name = models.CharField(max_length=80,blank=False, null=False)
    SSN_Number = models.CharField(max_length=10,blank=False, null=False, unique=True)
    Health_Insurance_Number = models.CharField(max_length=15,blank=True, null=True)
    Occupation = models.ForeignKey(Occupation,on_delete=models.CASCADE, max_length=10,blank=True, null=True)
    Employer_Name = models.CharField(max_length=80,blank=True, null=True)
    Employee_ID = models.CharField(max_length=15,blank=True, null=True)
    Emp_Address_1 = models.CharField(max_length=100,blank=True, null=True)
    Emp_Address_2 = models.CharField(max_length=100,blank=True, null=True)
    Emp_Country = models.ForeignKey(Country,on_delete=models.CASCADE, max_length=2,blank=True, null=True)
    Emp_Village = models.ForeignKey(Village,on_delete=models.CASCADE, max_length=10,blank=True, null=True)
    Income = models.ForeignKey(Income,on_delete=models.CASCADE, max_length=4,blank=True, null=True)
    Income_Frequency = models.ForeignKey(Income_Frequency,on_delete=models.CASCADE, max_length=10,blank=True, null=True)
    Legal_Status = models.ForeignKey(Legal_Status,on_delete=models.CASCADE, max_length=4,blank=True, null=True)
    Customer_Status = models.ForeignKey(Customer_Status,on_delete=models.CASCADE, max_length=4,blank=False, null=False)
    Date_Last_Modified = models.DateTimeField()
    def __str__(self) -> str:
        return self.user.first_name
        
    def clean(self):
        if not len(self.National_ID_Number) == 16:
            raise ValidationError(
                {'title': "Title should have at least 10 letters"})
