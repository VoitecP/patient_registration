from django import forms
from .models import *

class PatientSearchForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('name','sorting_date',)
        # exclude=['slug']  
          

    name=forms.CharField(max_length=50,label='Patient Name or Surname')
    SORT_CHOICES=[
        ('', 'None'),
        ('birth_date', 'Birth Date - Increase'),
        ('-birth_date', 'Birth Date - Decrease'),
    ]
    sorting_date=forms.ChoiceField(
        choices=SORT_CHOICES,
        widget=forms.RadioSelect,
        label='Sorting by Birth Date',
        )
    from_date=forms.DateField(
        required=False, 
        label='From Year',
        widget=forms.DateInput(format='%Y'),  # or full date '%d%m%Y'
        input_formats=['%Y'],
        )
    to_date=forms.DateField(
        required=False, 
        label='To Year',
        widget=forms.DateInput(format='%Y'),  # or full date '%d%m%Y'
        input_formats=['%Y'],
        )  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['sorting_date'].required = False

class DoctorSearchForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('name',) 
        # exclude=['slug']  

    name=forms.CharField(max_length=50,label='Doctor Name or Surname')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False

class VisitSearchForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ('patient_name','doctor_name','sorting_date',)
    
    patient_name=forms.CharField(max_length=50,label='Patient Name or Surname')
    doctor_name=forms.CharField(max_length=50,label='Doctor Name or Surname')
    SORT_CHOICES=[
        ('', 'None'),
        ('date', 'Date - Increase'),
        ('-date', 'Date - Decrease'),
    ]
    sorting_date=forms.ChoiceField(
        choices=SORT_CHOICES,
        widget=forms.RadioSelect,
        label='Sorting by Date',
        )
    from_date=forms.DateField(
        required=False, 
        label='From Year',
        widget=forms.DateInput(format='%Y'),  # or full date '%d%m%Y'
        input_formats=['%Y'],
        )
    to_date=forms.DateField(
        required=False, 
        label='To Year',
        widget=forms.DateInput(format='%Y'),  # or full date '%d%m%Y'
        input_formats=['%Y'],
        )  
    
    # CATEG_CHOICES=Category.objects.all().values_list('id','name')  # without choices manager
    CATEG_CHOICES= Category.choices_objects.all()
    categories=forms.MultipleChoiceField(
        choices=CATEG_CHOICES,widget=forms.CheckboxSelectMultiple,
        label='Categories'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient_name'].required = False
        self.fields['doctor_name'].required = False
        self.fields['sorting_date'].required = False
        self.fields['categories'].required = False
        
class CategorySearchForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',) 

    name=forms.CharField(max_length=50,label='Category Name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False    
    
    
    