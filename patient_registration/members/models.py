from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    PATIENT='PATIENT'
    DOCTOR='DOCTOR'
    
    ROLE_CHOICES=(
        (PATIENT,'Patient'),
        (DOCTOR,'Doctor'),
    )

    # username=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    role= models.CharField(max_length=30,choices=ROLE_CHOICES)

