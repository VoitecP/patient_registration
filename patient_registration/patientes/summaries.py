from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from collections import OrderedDict

def s_category(queryset):

	queryset=(OrderedDict(sorted(
		queryset
		.annotate(category_name=Coalesce('category__name', Value('-No Category-')))
		.order_by('category')
		.values('category_name')
		.annotate(sum=Sum('price'))
		.values_list('category_name','sum')))) 	
	return queryset

def s_year(queryset):

	queryset=(OrderedDict(sorted(
		queryset
		.values('date__year')
		.annotate(sum=Sum('price'))
		.order_by('date__year')
		.values_list('date__year', 'sum')))) 
	return queryset

def s_month(queryset):

	queryset=(
		queryset
		.values('date__month','date__year')
		.annotate(sum=Sum('price'))
		.values_list('date__month', 'date__year', 'sum')
		.order_by('date__year','date__month'))
	return queryset

def s_doctor(queryset):

	queryset=(queryset
		.values('doctor__name','doctor__surname','doctor__id')
		.annotate(sum=Sum('price'))
		.order_by('-sum')
		.values_list('doctor__name','doctor__surname','doctor__id', 'sum')) 
	return queryset

def s_total(queryset):
	queryset=queryset.aggregate(sum=Sum('price'))
	return queryset