from rest_framework import serializers
from patientes.models import *


class DoctorSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
        

class PatientSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Patient
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    patient_full_name=serializers.SerializerMethodField(read_only=True)
    doctor_full_name=serializers.SerializerMethodField(read_only=True)
    category_name=serializers.SerializerMethodField(read_only=True)
    # patient_id=serializers.SerializerMethodField(read_only=True)
    # patient=PatientSerializer(read_only=True)
   
    class Meta:
        model = Visit
        fields = '__all__'

    def get_patient_full_name(self, model):
        # return model.patient
        return model.patient.full_name


    def get_doctor_full_name(self, model):
        return model.doctor.full_name

    def get_category_name(self, model):
        if model.category == None:
            return None 
        else:
            return model.category.name

    # def get_patient_id(self, model):
    #     return model.patient.id





