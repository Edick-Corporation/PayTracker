from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View, ListView

from services.main_logic import get_type_list, filter_statistics_by_date_and_types, \
    user_is_anonymous, clear_users_types, get_ready_data_of_prices


def purchase_list_view(request):
    qs = filter_statistics_by_date_and_types
    if request.user.is_anonymous:
        return HttpResponseRedirect('/accounts/login')
    else:
        return render(request, 'purchase/list.html',  context={'purchase_list': qs})


class PurchaseList(ListView):
    """Отображение Покупок и Фильтра"""

    template_name = 'purchase/list.html'
    context_object_name = 'purchase_list'
    queryset = filter_statistics_by_date_and_types

    def get_queryset(self):
        try:
            return self.queryset
        except AttributeError:
            return HttpResponseRedirect('accounts/login/')


class PieChartV1(View):
    def get(self, request):

        labels = clear_users_types(self)
        data = get_ready_data_of_prices(self)
        print(data)
        return render(request, 'statistics/pie.html', {
            'labels': labels,
            'data': data
        })