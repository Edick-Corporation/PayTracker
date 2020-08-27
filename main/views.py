from django.views.generic import View, ListView

from main.forms import PurchaseAddForm
from main.utils import PurchaseListAndAddMixin
from services.main_logic import get_users_purchases, get_users_purchases_by_type, get_type_list


class PurchaseListAndAdd(PurchaseListAndAddMixin, View):
    """Отображение формы и Покупок в одном шаблоне"""

    form = PurchaseAddForm
    queryset = get_users_purchases
    template_name = 'purchase/list.html'


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
