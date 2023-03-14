from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from collections import OrderedDict
from .models import Visit
# from django.contrib.postgres.aggregates import ArrayAgg

def s_category(queryset):

	try:
		queryset=(OrderedDict(sorted(
			queryset
			.annotate(category_name=Coalesce('category__name', Value('-No Category-')))
			.order_by('category')
			.values('category_name')
			.annotate(sum=Sum('price'))
			.values_list('category_name','sum')))) 	
	except:
		pass
	return queryset

def s_year(queryset):

	try:
		queryset=(OrderedDict(sorted(
			queryset
			.values('date__year')
			.annotate(sum=Sum('price'))
			.order_by('date__year')
			.values_list('date__year', 'sum')))) 
	except:
		pass
	return queryset

def s_month(queryset):

	try:
		queryset=(
			queryset
			.values('date__month','date__year')
			.annotate(sum=Sum('price'))
			# .annotate(sum=Sum('visit__aggregate_table__price'))
			.values_list('date__month', 'date__year', 'sum')
			.order_by('date__year','date__month'))
	except:
		pass
	return queryset

def s_doctor(queryset):

	try:
		queryset=(queryset
			.values('doctor__name','doctor__surname','doctor__id')
			# .annotate(sum=Sum('visit__aggregate_table__price'))
			.annotate(sum=Sum('visit__price'))
			.order_by('-sum')
			.values_list('doctor__name','doctor__surname','doctor__id', 'sum')) 
	except:
		pass
	return queryset

def s_total(queryset):
	try:
		queryset=queryset.aggregate(sum=Sum('price'))
	except:
		pass
	return queryset