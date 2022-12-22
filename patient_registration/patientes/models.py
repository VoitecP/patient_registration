import datetime
import uuid
from django.db import models 



class VisitDoctorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(t_visit=models.Count('visit'))

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
        ordering=('surname',)

    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    phone=models.CharField(max_length=12)
    id=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    
    objects=models.Manager()     # Default manager for models
    # slug=models.SlugField(null=False, unique=True)     # <slug:slug>  path in URL 
    # prepopulated_fields={'slug':('name','surname')}
    
    @property
    def full_name(self):
        "Returns full name of Person"
        return '%s %s' % (self.name, self.surname)
    
    def __str__(self):
        return f'{self.full_name}'

    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"slug": self.slug})
    
class Patient(Person):
    citizen_id=models.CharField(max_length=11)
    birth_date=models.DateField()
    adress=models.CharField(max_length=80)
    city=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=5)
    id=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    
class Doctor(Person):
    specialization=models.CharField(max_length=12)
    visit_objects=VisitDoctorManager()
    # objects=models.Manager()
    
class Category(models.Model):
    class Meta:
        ordering=('name',)
    name=models.CharField(max_length=30, unique=True)
    objects=models.Manager()   # reverse error when no defined / commented
    choices_objects=ChoicesCategoryManager()
    id=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    def __str__(self):
        return f'{self.name}'

class Visit(models.Model):
    class Meta:
        ordering=('date',)

    id=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    date=models.DateTimeField(default=datetime.date.today)    
    patient=models.ForeignKey(Patient, models.PROTECT)
    doctor=models.ForeignKey(Doctor, models.PROTECT)
    description=models.TextField()
    price=models.CharField(max_length=10)
    category=models.ForeignKey(Category,models.PROTECT,null=True,blank=True)
    objects=models.Manager() 
    # object=models.Manager()  # Better to name as 'objects'
    # null_cat_object=NullCategoryManager()

    # id=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    def __str__(self):
        return f' Visit date: {self.date}, Price: {self.price}'




