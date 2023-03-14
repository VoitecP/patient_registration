from django.views.generic.list import ListView

from ..models import Visit
from ..summaries import *


class SummaryListView(ListView):
    model = Visit
    template_name='summary\summary_list.html'

    def get_context_data(self, object_list=None, *args, **kwargs):
        if object_list is not None: 
            queryset = object_list
        else: 
            queryset=self.object_list

        return super().get_context_data(
            s_category=s_category(queryset),
            s_month=s_month(queryset),  #
            s_year=s_year(queryset),
            s_doctor=s_doctor(queryset),  #
            s_total=s_total(queryset),
            *args,**kwargs)