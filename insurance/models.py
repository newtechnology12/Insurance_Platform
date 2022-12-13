from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer
import random

class InsurenceCategory(models.Model):
    category_name =models.CharField(max_length=20)
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.category_name

class Policy(models.Model):
    category= models.ForeignKey(InsurenceCategory, on_delete=models.CASCADE)
    policy_name=models.CharField(max_length=200)
    sum_assurance=models.PositiveIntegerField()
    premium=models.PositiveIntegerField()
    tenure=models.PositiveIntegerField()
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.policy_name

class PolicyRecord(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    Policy= models.ForeignKey(Policy, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,default='Pending')
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.policy

class VehicleCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, null = True)

    def __str__(self) -> str:
        return self.name

class CoverIdentification(models.Model):
    vehicle_usage = models.ForeignKey(VehicleCategory, on_delete=models.PROTECT, max_length=255, blank=True,null=True)
    vehicleManufacture_year = models.CharField(max_length=255,default='2022', blank=True,null=True)
    vehicleBrand = models.CharField(max_length=255,default='HYUNDAI', blank=True,null=True)
    vehicleModel = models.CharField(max_length=255,default='SONATA', blank=True,null=True)
    vehiclePlateNo = models.CharField(max_length=10,default='RAF98D',blank=True,null=True)
    vehicle_chassisNo = models.CharField(max_length=255,default='GJG86FS', blank=True,null=True)
    vehicle_seat_capacity = models.CharField(max_length=255,default='5', blank=True,null=True)
    vihecleImage = models.ImageField(upload_to='media/%Y/%m/%d/',max_length=70, blank=True)
    documents = models.FileField()
    sumInsured = models.CharField(max_length=2555,default='00,000.00',blank=True,null=True) 
    def __str__(self) -> str:
        return self.vehicle_usage
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

SELECT_COVERS = (
    ('THIRD PART LIABILITY','Third Part Liability'),
    ('OWN DAMAGE','Own Damage'),
    ('THEFT','Theft'),
    ('FIRE','Fire'),
    ('OCCUPANT', 'OCCUPANT'),
    ('TPL+','Tpl+'),
)

DURATION = (
    ('1-2-9 Months','1-2-9 Months'),
    ('1-6 Months','1-6 Months'),
    ('1-3 Months','1-3 Months'),
)
class Primium(models.Model):
    cust_id = models.CharField(max_length=70,default='cust'+str(random.randrange(10000,99999,1)))
    STATUS = (('approved','APPROVED'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
    duration = models.CharField(choices=DURATION,default='1-6 Months',max_length=255, blank=True, null=True)
    locationCover = models.CharField(max_length=2555, default='Rwanda',blank=True, null=True)
    declared_value_or_sumInsured = models.PositiveIntegerField(default=0)
    selectCovers = models.CharField(max_length=255, blank=True, null=True, choices=SELECT_COVERS, default='THIRD PART LIABILITY') 
    numberOfOccupation_covered = models.PositiveIntegerField(default=1)
    sum_insuredPerOccupanr = models.CharField(max_length=255,default='3-Million-Rwf', blank=True, null=True)
    starting_date =models.DateField(auto_now=True)
    ending_date =models.DateField(auto_now=True)
    status = models.CharField(max_length=30, blank = True, null=True, default='pending')

    def __str__(self) -> str:
        return self.duration


class Insured(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.PROTECT,related_name='Insured', max_length=255, blank=True,null=True)
    ownertype = models.CharField(max_length=2555,blank=True,null=True)
    vehicleClassification = models.CharField(max_length=2555,blank=True,null=True)
    vehicle_usage = models.CharField(max_length=2555,blank=True,null=True)
    vehicleManufacture_year = models.CharField(max_length=2555,blank=True,null=True)
    vehicleBrand = models.CharField(max_length=2555,blank=True,null=True)
    vehicleModel = models.CharField(max_length=2555,blank=True,null=True)
    vehicle_chassisNo = models.CharField(max_length=2555,blank=True,null=True)
    vehicle_seat_capacity = models.CharField(max_length=2555,blank=True,null=True)
    #ABOUT POLICES
    duration = models.CharField(max_length=2555,blank=True,null=True)
    locationCover = models.CharField(max_length=2555,blank=True,null=True)
    STATUS = (('approved','APPROVED'),('pending','PENDING'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
    declared_value_or_sumInsured = models.CharField(max_length=2555,blank=True,null=True) 
    numberOfOccupation_covered = models.PositiveIntegerField()
    accidentDeath = models.CharField(max_length=2555,blank=True,null=True) 
    totalNatePremium = models.CharField(max_length=2555,blank=True,null=True)
    medicalFess = models.CharField(max_length=2555,default='00,000.00',blank=True,null=True) 
    motoGuarantyFound = models.CharField(max_length=2555,blank=True,null=True)
    vat =  models.CharField(max_length=2555,blank=True,null=True)
    totalPremiumPayable = models.CharField(max_length=2555,default='00,000.00',blank=True,null=True)
    documents = models.FileField()
    status = models.CharField(choices=STATUS,  default='pending',max_length=15)

    def __str__(self) -> str:
        return f'{self.ownertype} and {self.vehicleClassification}'
    
    def totalPremiumPayable():
        pass

    def vat():
        pass
    def motoGuarantyFound():
        pass
    def totalNatePremium():
        pass
    def netPremium():
        pass

class FeedBack_customer(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    description =models.CharField(max_length=500)
    admin_comment=models.CharField(max_length=200,default='Nothing')
    asked_date =models.DateField(auto_now=True)
    
    def __str__(self):
        return self.description

class FeedBack(models.Model): 
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    admin_comment=models.TextField(max_length=300,default='Nothing')
    asked_date =models.DateField(auto_now=True)