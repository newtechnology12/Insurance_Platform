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

GENDER = (
    ('Male', 'MALE'),
    ('Female','Female'),
    ('Corporate','Corporate'),

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

class Education(models.Model):
    education = models.CharField(max_length=255,blank=True,null=True)

class ProfessionDetails(models.Model):
    detailsName = models.CharField(max_length=255, blank=True, null=True)

class Profession(models.Model):
    professionName = models.ManyToManyField(ProfessionDetails)

    def list_Profession(self, obj):
        return "\n".join([str(p).professionName for p in obj.professionName.all()])

client_status=(
    ('Active','Active'),
    ('Inactive','Inactive'),
    ('Delete','Delete'),
    )
    

class PersonalProfile(models.Model):
    identification = models.CharField(max_length=255,blank=True, null=False, choices=ID_TYPE)
    identificationId = models.CharField(max_length=255,blank=True, null=False)
    title = models.CharField(max_length=255,blank=True, null=False)
    sex = models.CharField(max_length=255,blank=True, null=False, choices=GENDER)
    dateofbirth = models.DateField(max_length=255,blank=True, null=False)
    profession = models.ForeignKey(Profession,on_delete = models.PROTECT, max_length=255,blank=True, null=False)
    education = models.ForeignKey(Education,on_delete = models.PROTECT, max_length=255,blank=True, null=False)
    prefered_language = models.CharField(max_length=255,blank=True, null=False, choices = prefered_language)
    province = models.CharField(max_length=255,blank=True, null=False)
    district = models.CharField(max_length=255,blank=True, null=False)
    sector = models.CharField(max_length=255,blank=True, null=False)
    cell = models.CharField(max_length=255,blank=True, null=False)
    village = models.CharField(max_length=255,blank=True, null=False)
    civil_status = models.CharField(max_length=255,blank=True, null=False, choices=civil_status)
    client_status = models.CharField(max_length=255,blank=True, null=False, choices=client_status)

class Customer(AbstractBaseUser):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=255,blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255,blank=True, null=False)
    mobile = models.CharField(max_length=20,blank=True, null=False)
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
        return str(self.firstName)
        # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name

