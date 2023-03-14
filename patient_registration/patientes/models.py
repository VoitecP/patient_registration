import datetime
import uuid
from django.db import models 
from django.urls import reverse
from django.template.defaultfilters import slugify


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
    

    name=models.CharField(max_length=30, default='')
    surname=models.CharField(max_length=30,  default='')
    phone=models.CharField(max_length=12)
    id=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    objects=models.Manager()     # Default manager for models
    slug=models.SlugField(null=True, unique=True, editable=False)     # <slug:slug>  path in URL 
    # prepopulated_fields={'slug':('name','surname')}
    
    @property
    def full_name(self):
        "Returns full name of Person"
        return '%s %s' % (self.name, self.surname)
    
    def __str__(self):
        return f'{self.full_name}'

    def get_absolute_url(self):
        name=self.__class__.__name__.lower()
        return reverse('patientes:'+name+'-detail-slug', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        # if not self.slug:
        self.slug=slugify(self.full_name+ "-" + str(self.id)[0:5])
        return super().save(*args,**kwargs)

    
    
class Patient(Person):

    citizen_id=models.CharField(max_length=11)
    birth_date=models.DateField(default=datetime.date.today())
    adress=models.CharField(max_length=80)
    city=models.CharField(max_length=20)
    zip_code=models.CharField(max_length=5)
    # id=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

        
    

class Doctor(Person):
    specialization=models.CharField(max_length=12)
    visit_objects=VisitDoctorManager()
    # objects=models.Manager()
    
   

class Category(models.Model):
    class Meta:
        ordering=('name',)
    name=models.CharField(max_length=30, unique=True, default='')
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
    patient=models.ForeignKey(Patient, models.PROTECT, default='')
    doctor=models.ForeignKey(Doctor, models.PROTECT, default='')
    description=models.TextField()
    price=models.CharField(max_length=10)
    category=models.ForeignKey(Category,models.PROTECT,null=True,blank=True, default='')
    objects=models.Manager() 
    # object=models.Manager()  # Better to name as 'objects'
    # null_cat_object=NullCategoryManager()

    # id=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, unique=True)

    def __str__(self):
        return f' Visit date: {self.date}, Price: {self.price}'




