from django.shortcuts import render
from django.views.generic import View, ListView

from services.main_logic import get_users_purchases_by_type, get_type_list, filtering_by_date


class PurchaseList(ListView):
    """Отображение Покупок и Фильтра"""
    queryset = filtering_by_date
    template_name = 'purchase/list.html'
    context_object_name = 'purchase_list'


class TypeList(ListView):
    """Отображение всех Типов"""
    template_name = 'purchase/types.html'
    context_object_name = 'type_list'
    queryset = get_type_list()


class PurchasesByTypeList(ListView):
    """Отображение Покупок определенного Типа"""
    template_name = 'purchase/purchases_by_type.html'
    context_object_name = 'purchases_by_type'
    queryset = get_users_purchases_by_type
