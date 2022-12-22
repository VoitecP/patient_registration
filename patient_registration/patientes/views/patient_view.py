from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ..models import Patient
from ..forms import PatientSearchForm
 
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q, ProtectedError
from django.shortcuts import render


class UUIDMixin(SingleObjectMixin):
    def get_object(self):
        return self.model.objects.get(id=self.kwargs.get("id"))

class SlugMixin(SingleObjectMixin):
    def get_object(self):
        return self.model.objects.get(slug=self.kwargs.get("slug"))

class PatientCreateView(CreateView):
    model = Patient
    fields='__all__'
    success_url=reverse_lazy('patientes:patient-list')
    template_name='patient\patient_form.html'

class PatientUpdateView(UUIDMixin, UpdateView):
    model = Patient    
    fields='__all__'
    success_url=reverse_lazy('patientes:patient-list')
    template_name='patient\patient_update_form.html'

class PatientDeleteView(UUIDMixin,DeleteView):
    model = Patient    
    success_url=reverse_lazy('patientes:patient-list')
    template_name='patient\patient_confirm_delete.html'

    def post(self, request,*args, **kwargs):
        object = self.get_object()
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, "Django Message - Protected error, ups")
            return render(request, 'patient\patient_error_delete.html', {'object': object})

class PatientDetailView(UUIDMixin, DetailView):
    model = Patient
    template_name='patient\patient_detail.html'

class PatientSlugDetailView(SlugMixin, DetailView):
    model = Patient
    template_name='patient\patient_detail.html'

class PatientListView(ListView):
    model = Patient
    paginate_by = 5
    template_name='patient\patient_list.html'

    def get_context_data(self, *,object_list=None, **kwargs):
        if object_list is not None: 
            queryset = object_list
        else: 
            queryset=self.object_list

        form=PatientSearchForm(self.request.GET)
        if form.is_valid(): 
            name=form.cleaned_data.get('name')
            sorting_date=form.cleaned_data.get('sorting_date')
            from_date = form.cleaned_data.get('from_date') #  from_date form return's 01-01-yyyy
            to_date = form.cleaned_data.get('to_date')
            if name:
                queryset=queryset.filter(Q(name__icontains=name) | Q(surname__icontains=name))
            if sorting_date:
                queryset=queryset.order_by(sorting_date)
            if  from_date:   # birth_date__year__gte  - only year filter required number data-form
                queryset = queryset.filter(birth_date__gte=from_date)  
            if  to_date:
                queryset = queryset.filter(birth_date__lte=to_date)

        return super().get_context_data(
            form=form,
            object_list=queryset,
            **kwargs)