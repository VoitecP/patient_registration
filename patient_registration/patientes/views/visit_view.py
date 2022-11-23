from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ..models import Visit
from ..forms import VisitSearchForm

from django.urls import reverse_lazy
from django.db.models import Q


class VisitCreateView(CreateView):
    model = Visit
    fields='__all__'
    success_url=reverse_lazy('patientes:visit-list')
    template_name='visit/visit_form.html'   # default path: \patientes\templates\patientes\visit_form,html

class VisitUpdateView(UpdateView):
    model = Visit    
    fields='__all__'
    success_url=reverse_lazy('patientes:visit-list')
    template_name='visit/visit_update_form.html'

class VisitDeleteView(DeleteView):
    model = Visit  
    success_url=reverse_lazy('patientes:visit-list')
    template_name='visit/visit_confirm_delete.html'

class VisitDetailView(DetailView):
    model = Visit
    template_name='visit/visit_detail.html'

class VisitListView(ListView):
    model = Visit
    paginate_by = 5
    template_name='visit/visit_list.html'

    def get_context_data(self, *,object_list=None, **kwargs):
        if object_list is not None: 
            queryset = object_list
        else: 
            queryset=self.object_list

        form=VisitSearchForm(self.request.GET)
        if form.is_valid(): 
            patient_name=form.cleaned_data.get('patient_name')  # 'patient' will show list of Patient models
            doctor_name=form.cleaned_data.get('doctor_name')
            sorting_date=form.cleaned_data.get('sorting_date')
            from_date = form.cleaned_data.get('from_date') #  from_date form return's 01-01-yyyy  
            to_date = form.cleaned_data.get('to_date')  # warning about Naive Time Zone in Console
            categories = form.cleaned_data.get('categories') 
            if patient_name:
                queryset=queryset.filter(Q(patient__name__icontains=patient_name) | Q(patient__surname__icontains=patient_name))
            if doctor_name:
                queryset=queryset.filter(Q(doctor__name__icontains=doctor_name) | Q(doctor__surname__icontains=doctor_name))
            if sorting_date:
                queryset=queryset.order_by(sorting_date)
            if from_date:   # date__year__gte  - only year filter required number data-form
                queryset = queryset.filter(date__gte=from_date)  
            if to_date:
                queryset = queryset.filter(date__lte=to_date)
            if categories:
                queryset = queryset.filter(Q(category__id__in=categories))

        return super().get_context_data(
            form=form,
            object_list=queryset,
            **kwargs)
    