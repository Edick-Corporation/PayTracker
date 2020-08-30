from django.shortcuts import render, redirect
from django.views.generic import View, ListView

from services.main_logic import get_users_purchases_by_type, get_type_list, shopping_filter_calendar, user_is_anonymous, \
    get_users_purchases


class PurchaseList(ListView):
    """Отображение Покупок и Фильтра"""

    template_name = 'purchase/list.html'
    context_object_name = 'purchase_list'
    queryset = user_is_anonymous(obj=shopping_filter_calendar)


class TypeList(ListView):
    """Отображение всех Типов"""

    template_name = 'purchase/types.html'
    context_object_name = 'type_list'
    queryset = get_type_list()


class PurchasesByTypeList(ListView):
    """Отображение Покупок определенного Типа"""

    template_name = 'purchase/purchases_by_type.html'
    context_object_name = 'purchases_by_type'

    def get_queryset(self):
        return user_is_anonymous(obj=get_users_purchases_by_type)
