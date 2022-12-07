from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer

class Category(models.Model):
    category_name =models.CharField(max_length=20)
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.category_name

class Policy(models.Model):
    category= models.ForeignKey('Category', on_delete=models.CASCADE)
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

class VehicleIdentification(models.Model):
    ownertype = models.ForeignKey(VehicleCategory,on_delete= models.DO_NOTHING, max_length=255, blank=True,null=True)
    vehicleClassification = models.CharField(max_length=255, blank=True,null=True)
    vehicle_usage = models.CharField(max_length=255, blank=True,null=True)
    usage_type = models.CharField(max_length=255, blank=True,null=True)
    vehicleManufacture_year = models.CharField(max_length=255, blank=True,null=True)
    vehicleBrand = models.CharField(max_length=255, blank=True,null=True)
    vehicleModel = models.CharField(max_length=255, blank=True,null=True)
    vehicle_chassisNo = models.CharField(max_length=255, blank=True,null=True)
    vehicle_seat_capacity = models.CharField(max_length=255, blank=True,null=True)

SELECT_COVERS = (
    ('THIRD PART LIABILITY','Third Part Liability'),
    ('OWN DAMAGE','Own Damage'),
    ('THEFT','Theft'),
    ('FIRE','Fire'),
    ('OCCUPANT', 'OCCUPANT'),
    ('TPL+','Tpl+'),
)


class InsuranceCovers(models.Model):
    duration = models.CharField(max_length=255, blank=True, null=True)
    locationCover = models.CharField(max_length=2555, blank=True, null=True)
    declared_value_or_sumInsured = models.CharField(max_length=255, blank=True, null=True) 
    numberOfOccupation_covered = models.PositiveIntegerField()
    sum_insuredPerOccupanr = models.CharField(max_length=255, blank=True, null=True)
    selectCovers = models.CharField(max_length=255, blank=True, null=True, choices=SELECT_COVERS)
    starting_date =models.DateField(auto_now=True)
    ending_date =models.DateField(auto_now=True)

    

class Insured(models.Model):
    ownertype = models.CharField(max_length=2555,blank=True,null=True)
    vehicleClassification = models.CharField(max_length=2555,blank=True,null=True)
    vehicle_usage = models.CharField(max_length=2555,blank=True,null=True)
    usage_type = models.CharField(max_length=2555,blank=True,null=True)
    vehicleManufacture_year = models.CharField(max_length=2555,blank=True,null=True)
    vehicleBrand = models.CharField(max_length=2555,blank=True,null=True)
    vehicleModel = models.CharField(max_length=2555,blank=True,null=True)
    vehicle_chassisNo = models.CharField(max_length=2555,blank=True,null=True)
    vehicle_seat_capacity = models.CharField(max_length=2555,blank=True,null=True)

    duration = models.CharField(max_length=2555,blank=True,null=True)
    locationCover = models.CharField(max_length=2555,blank=True,null=True)
    declared_value_or_sumInsured = models.CharField(max_length=2555,blank=True,null=True) 
    numberOfOccupation_covered = models.PositiveIntegerField()
    selectCovers = models.CharField(max_length=2555, blank=True, null=True, choices=SELECT_COVERS)
    totalNatePremium = models.CharField(max_length=2555,blank=True,null=True)
    motoGuarantyFound = models.CharField(max_length=2555,blank=True,null=True)
    vat =  models.CharField(max_length=2555,blank=True,null=True)
    totalPremiumPayable = models.CharField(max_length=2555,blank=True,null=True)

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

class Question(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    description =models.CharField(max_length=500)
    admin_comment=models.CharField(max_length=200,default='Nothing')
    asked_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.description