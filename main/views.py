from django.shortcuts import render, redirect
from django.views.generic import View, ListView

from services.main_logic import get_type_list, filter_statistics_by_date_and_types, \
    user_is_anonymous


class PurchaseList(ListView):
    """Отображение Покупок и Фильтра"""

    template_name = 'purchase/list.html'
    context_object_name = 'purchase_list'
    queryset = filter_statistics_by_date_and_types
