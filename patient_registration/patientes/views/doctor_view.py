from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ..models import Doctor
from ..forms import DoctorSearchForm

from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q, ProtectedError
from django.shortcuts import render

class DoctorCreateView(CreateView):
    model = Doctor
    fields='__all__'
    success_url=reverse_lazy('patientes:doctor-list')
    template_name='doctor\doctor_form.html'

class DoctorUpdateView(UpdateView):
    model = Doctor    
    fields='__all__'
    success_url=reverse_lazy('patientes:doctor-list')
    template_name='doctor\doctor_update_form.html'

class DoctorDeleteView(DeleteView):
    model = Doctor    
    success_url=reverse_lazy('patientes:doctor-list')
    template_name='doctor\doctor_confirm_delete.html'

    def post(self, request,*args, **kwargs):
        object = self.get_object()
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, "Django Message - Protected error, ups")
            return render(request, 'doctor\doctor_error_delete.html', {'object': object})

class DoctorListView(ListView):
    model = Doctor
    paginate_by = 5
    template_name='doctor\doctor_list.html'

    def get_context_data(self, *,object_list=None, **kwargs):
        if object_list is not None: 
            queryset = object_list
        else: 
            queryset=self.object_list
        form=DoctorSearchForm(self.request.GET)
        if form.is_valid(): 
            name=form.cleaned_data.get('name')
            if name:
                queryset=queryset.filter(Q(name__icontains=name) | Q(surname__icontains=name))

        return super().get_context_data(
            form=form,
            object_list=queryset,
            **kwargs)

class DoctorDetailView(DetailView):
    model = Doctor
    template_name='doctor\doctor_detail.html'