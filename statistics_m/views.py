from django.views.generic import View
from django.shortcuts import render

from services.main_logic import get_form_to_record_purchase,  get_type_list, filter_statistics_by_date_and_types, \
    add_purchase, get_name_of_types, get_ready_data_of_prices, get_filtered_qs_by_date
from services.optimization_logic import get_ready_average
from statistics_m.utils import PurchaseListAndAddMixin, PieChartAndAddMixin


class PieChartAndPurchases(PieChartAndAddMixin, View):
    labels = get_name_of_types
    data = get_ready_data_of_prices
    qs = get_filtered_qs_by_date
    post_form = add_purchase
    template_name = 'statistics/pie.html'
    form = get_form_to_record_purchase()


class StatisticsListAndAdd(PurchaseListAndAddMixin, View):
    """Отображение Формы, Статистики и Фильтра в одном шаблоне"""

    queryset = filter_statistics_by_date_and_types
    types = get_type_list()
    average = get_ready_average
    template_name = 'statistics/statistics.html'


