from django.views.generic import View

from services.main_logic import get_form_to_record_purchase,  get_type_list, filter_statistics_by_date_and_types, \
    add_purchase
from services.optimization_logic import get_ready_average

from statistics_m.utils import PurchaseListAndAddMixin


class StatisticsListAndAdd(PurchaseListAndAddMixin, View):
    """Отображение Формы, Статистики и Фильтра в одном шаблоне"""

    form = get_form_to_record_purchase()
    post_form = add_purchase
    queryset = filter_statistics_by_date_and_types
    types = get_type_list()
    average = get_ready_average
    template_name = 'statistics/statistics.html'






