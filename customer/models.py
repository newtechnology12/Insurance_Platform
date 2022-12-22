from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.timezone import now
from django.utils import timezone


class MyAccountManager(BaseUserManager):
    def create_user(self,firstName,lastName,username,email,phone,address,password=None,confirmPassword=None,):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        if not firstName:
            raise ValueError('Users must have a firstName')

        if not lastName:
            raise ValueError('Users must have a lastName')
        
        if not phone:
            raise ValueError('Users must have a phone')
        
        if not address:
            raise ValueError('Users must have a address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(confirmPassword)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,mobile,Password):
        user = self.create_user(
            username = username,
            mobile = mobile,
            email=self.normalize_email(email),
            Password=Password,
         
            
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



civil_status = (
    ('Married', 'Married'),
    ('Widowed','Widowed'),
    ('Separated','Separated'),
    ('Divorced','Divorced'),
    ('Single','Single'),
    ('Not Applicable','Not Applicable'),

)

ID_TYPE = (
    ('Driving_License','Driving_License'),
    ('Rwandan Nationals','Rwandan Nationals'),
    ('Refugee ID','Refugee ID'),
    ('Passport','Passport'),
    ('ForeignerID','ForeignerID'),
    ('Registration Number','Registration Number')
    
)
prefered_language = (
    ('KINYARWANDA','Kinyarwanda'),
    ('ENGLISH','English'),
    ('SWAHILI','Swahili'),   
)

TITLE = (
    ('Miss','Miss'),
    ('Mister','Mister'),
    ('Mrs','Mrs'),
    ('Miss/Mrs','Miss/Mrs'),
    ('Company','Company'),
    ('Joint/Group Acc','Joint/Group Acc'),   
)

class Education(models.Model):
    Education_Description = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self) -> str:
        return self.Education_Description
class Occupation(models.Model):
    Occupation_Description = models.CharField(max_length=255, blank=True, null=True)
       
    def __str__(self) -> str:
        return self.Occupation_Description

class OccupationSub(models.Model):
    Occupation_Description = models.CharField(max_length=255, blank=True,null=True)
    subOccupation_Description = models.ForeignKey(Occupation,on_delete=models.PROTECT,blank=True,null=True)


    def list_Profession(self, obj):
        return "\n".join([str(p).subOccupation_Description for p in obj.subOccupation_Description.all()])
    
    def __str__(self) -> str:
        return self.Occupation_Description


client_status=(
    ('Active','Active'),
    ('Inactive','Inactive'),
    ('Delete','Delete'),
    )
class Country(models.Model):
    countryname = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self) -> str:
        return self.countryname 

class Province(models.Model):
    Provincename = models.CharField(max_length=255, blank=True,null=True)
    Country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True,null=True)
    def __str__(self) -> str:
        return self.Provincename   
class District(models.Model):
    districtname = models.CharField(max_length=255, blank=True,null=True)  
    province = models.ForeignKey(Province, on_delete=models.PROTECT, blank=True,null=True)
    Country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True,null=True)
    
    def __str__(self) -> str:
        return self.districtname 
class Sector(models.Model):
    sectorname = models.CharField(max_length=255, blank=True,null=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT, blank=True,null=True)

    def __str__(self) -> str:
        return self.sectorname 

   
class Cell(models.Model):
    cellname = models.CharField(max_length=255, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT, blank=True,null=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, blank=True,null=True)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, blank=True,null=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT, blank=True,null=True)
    Country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True,null=True)

    def __str__(self) -> str:
        return self.cellname 

class Village(models.Model):
    villagename = models.CharField(max_length=255, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT, blank=True,null=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, blank=True,null=True)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, blank=True,null=True)
    Country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True,null=True)

    def __str__(self) -> str:
        return self.villagename 
INITIALS= ( 
("MISS","Miss"),
("MR","Mister"),
("MRS","Mrs"),
("MS","Miss/Mrs"),
("CORP","Company"),
("J","Joint/Group Acc")
)

STATUS = (('Corporate Custome','Corporate Custome'),('Individual Customer','Individual Customer'))
class PersonalProfile(models.Model):
    
    
    classification = models.CharField(max_length=255,blank=True, null=False)
    initials = models.CharField(max_length=255,blank=True, null=False, choices=INITIALS)
    firstName = models.CharField(max_length=255, blank=True, null=True)
    middleName = models.CharField(max_length=255, blank=True, null=True)
    lastName = models.CharField(max_length=255, blank=True, null=True)
    fullName = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    id_type = models.CharField(max_length=255,blank=True, null=False, choices=ID_TYPE)
    idNumber = models.CharField(max_length=255,blank=True, null=False)
    id_picture = models.ImageField()
    postaddres=models.CharField(max_length=255,blank=True, null=False)
    nationality= models.CharField(max_length=255, blank=True, null=True)
    placeOfBirth =  models.CharField(max_length=255, blank=True, null=True)
    PostalAddress=models.CharField(max_length=255,blank=True, null=False)
    postcode=models.CharField(max_length=255,blank=True, null=False)
    physicalAddres =  models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255,blank=True, null=False, choices=TITLE)
    sex = (("M","MALE"),("F","FEMALE"))
    dateofbirth = models.DateField(max_length=255,blank=True, null=False)
    education = models.ForeignKey(Education,on_delete = models.PROTECT, max_length=255,blank=True, null=False)
    prefered_language = models.CharField(max_length=255,blank=True, null=False, choices = prefered_language)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True,null=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT, blank=True,null=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, blank=True,null=True)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, blank=True,null=True)
    cell = models.ForeignKey(Village, on_delete=models.PROTECT, blank=True,null=True)
    village = models.ForeignKey(Cell, on_delete=models.PROTECT, blank=True,null=True)
    ton =  models.CharField(max_length=255, blank=True, null=True)
    MaritalStatus = models.CharField(max_length=255,blank=True, null=False, choices=civil_status)
    client_status = models.CharField(max_length=255,blank=True, null=False, choices=client_status)
    activitySector = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    SubSectors = models.CharField(max_length=255, blank=True, null=True)
    ContactPerson = models.CharField(max_length=255, blank=True, null=True)
    NextofKin = models.CharField(max_length=255, blank=True, null=True) 
    NextofKinContacts = models.CharField(max_length=255, blank=True, null=True) 
    comopanyName =models.CharField(max_length=255, blank=True, null=True)
    tinDocument = models.ImageField()
    
    def __str__(self) -> str:
        return self.user.first_name

class Customer(AbstractBaseUser):
    username=models.CharField(max_length=255,blank=True, null=True,unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True,unique=True)
    password = models.CharField(max_length=255,blank=True, null=False)
    mobile = models.CharField(max_length=20,blank=True, null=False,unique=True)
    date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','email','mobile']

    objects = MyAccountManager()


    def __str__(self):
        return str(self.username)
        # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

   
    @property
    def get_name(self):
        return self.email+" "+self.username
    @property
    def get_instance(self):
        return self
    

