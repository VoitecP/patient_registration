from django.contrib import admin
from .models import *
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    # list_display = ("name","surname",)
    prepopulated_fields={'slug':('name','surname')}
    # readonly_fields=('slug',)
    
class DoctorAdmin(admin.ModelAdmin):
    # list_display = "__all__"
    prepopulated_fields={'slug':('name','surname')}
    # readonly_fields=('slug',)

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)

# admin.site.register(Patient)
# admin.site.register(Doctor)
admin.site.register(Visit)
admin.site.register(Category)

# class Patient