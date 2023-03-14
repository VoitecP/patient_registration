from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from ..forms import CategorySearchForm
from ..models import Category


from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.shortcuts import render


class UUIDMixin(SingleObjectMixin):
    
    def get_object(self):
        return self.model.objects.get(id=self.kwargs.get("id"))

class CategoryCreateView(CreateView):
    model = Category
    fields='__all__'
    success_url=reverse_lazy('patientes:category-list')
    template_name='category/category_form.html'

class CategoryUpdateView(UUIDMixin,UpdateView):
    model = Category    
    fields='__all__'
    success_url=reverse_lazy('patientes:category-list')
    template_name='category/category_update_form.html'

class CategoryDeleteView(UUIDMixin,DeleteView):
    model = Category  
    success_url=reverse_lazy('patientes:category-list')
    template_name='category/category_confirm_delete.html'

    def post(self, request,*args, **kwargs):
        object = self.get_object()
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, "Django Message - Protected error, ups")
            return render(request, 'patientes\category_error_delete.html', {'object': object})


class CategoryDetailView(UUIDMixin,DetailView):
    model = Category
    template_name='category/category_detail.html'

class CategoryListView(ListView):
    model = Category
    paginate_by = 5
    template_name='category/category_list.html'

    def get_context_data(self, *,object_list=None, **kwargs):
        if object_list is not None: 
            queryset = object_list
        else: 
            queryset=self.object_list
        form=CategorySearchForm(self.request.GET)
        if form.is_valid(): 
            name=form.cleaned_data.get('name')
            if name:
                queryset=queryset.filter(name__icontains=name)

        return super().get_context_data(
            form=form,
            object_list=queryset,
            **kwargs)
