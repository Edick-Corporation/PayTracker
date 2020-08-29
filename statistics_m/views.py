from django.views.generic import View

from statistics_m.forms import PurchaseAddForm
from services.main_logic import shopping_filter_calendar, get_form_to_record_purchase
from statistics_m.utils import PurchaseListAndAddMixin


class StatisticsListAndAdd(PurchaseListAndAddMixin, View):
    """Отображение Формы, Статистики и Фильтра в одном шаблоне"""

    form = get_form_to_record_purchase
    queryset = shopping_filter_calendar
    template_name = 'statistics/statistics.html'
