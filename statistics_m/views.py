from django.shortcuts import render
from django.views.generic import View

from services.main_logic import get_form_to_record_purchase,  get_type_list, filter_statistics_by_date_and_types, \
    add_purchase
from statistics_m.utils import PurchaseListAndAddMixin
from services.optimization_logic import count_average_expenses_by_week


class StatisticsListAndAdd(PurchaseListAndAddMixin, View):
    """Отображение Формы, Статистики и Фильтра в одном шаблоне"""

    form = get_form_to_record_purchase()
    post_form = add_purchase
    queryset = filter_statistics_by_date_and_types
    types = get_type_list()
    average = count_average_expenses_by_week
    template_name = 'statistics/statistics.html'




