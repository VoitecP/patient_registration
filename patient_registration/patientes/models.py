import datetime
from django.db import models 
from django.db.models import Count

class VisitDoctorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(t_visit=Count('visit'))

class ChoicesCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().values_list('id','name')

# Why not ? :)
# class NullCategoryManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(category__isnull=True)

class Person(models.Model):  #  Abstract Model 
    class Meta:
        abstract=True
        ordering=('pk',)

    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    phone=models.CharField(max_length=12)
    objects=models.Manager()     # Default manager for models
    
    @property
    def full_name(self):
        "Returns full name of Person"
        return '%s %s' % (self.name, self.surname)
    
    def __str__(self):
        return f'{self.full_name}'

class Patient(Person):
    
    citizen_id=models.CharField(max_length=11)
    birth_date=models.DateField()
    adress=models.CharField(max_length=80)
    city=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=5)
    
class Doctor(Person):
   
    specialization=models.CharField(max_length=12)
    visit_objects=VisitDoctorManager()
    # objects=models.Manager()
    
class Category(models.Model):
    class Meta:
        ordering=('pk',)

    name=models.CharField(max_length=30, unique=True)
    object=models.Manager()   # reverse error when no defined / commented
    choices_objects=ChoicesCategoryManager()

    def __str__(self):
        return f'{self.name}'

class Visit(models.Model):
    class Meta:
        ordering=('pk',)

    date=models.DateTimeField(default=datetime.date.today)    
    patient=models.ForeignKey(Patient, models.PROTECT)
    doctor=models.ForeignKey(Doctor, models.PROTECT)
    description=models.TextField()
    price=models.CharField(max_length=10)
    category=models.ForeignKey(Category,models.PROTECT,null=True,blank=True)
    object=models.Manager() 
    # null_cat_object=NullCategoryManager()

    def __str__(self):
        return f' ID {self.pk}, Price: {self.price}'




