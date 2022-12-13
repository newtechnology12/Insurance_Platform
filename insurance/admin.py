from django.contrib import admin
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin


from django.contrib import admin
from .models import *
from customer.models import  *

admin.site.register(InsurenceCategory)
admin.site.register(Policy)
admin.site.register(PolicyRecord)
admin.site.register(Customer)


@admin.register(VehicleCategory)
class VehicleCategoryAdmin(ImportExportModelAdmin):
    list_display = ['name']

admin.site.register(Primium)
admin.site.register(CoverIdentification)
admin.site.register(Insured)
@admin.register(Education)
class EducationAdmin(ImportExportModelAdmin):
    list_display = ['Education_Description']


@admin.register(ProfessionsubOccupation_Description)
class ProfessionDetailsAdmin(ImportExportModelAdmin):
    list_display = ['ProfessionsubOccupation_Description']


@admin.register(Profession)
class ProfessionAdmin(ImportExportModelAdmin):
    list_display = ['list_Profession']
    
@admin.register(PersonalProfile)
class PersonalProfileAdmin(ImportExportModelAdmin):
    list_display = ['identification','identificationId','title','sex','dateofbirth','profession', 'education','prefered_language','province','district','sector','cell','village','civil_status']

admin.site.register(FeedBack_customer)
admin.site.register(FeedBack)

admin.site.site_header = 'ADM Page Of Shaka.rw Platform.'
admin.site.site_title = 'Welcome To Shaka.rw Platform.'
admin.site.index_title = 'Welcome To Shaka.rw Platform.'