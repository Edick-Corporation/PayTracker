from django.views.generic import View, ListView

from statistics_m.forms import PurchaseAddForm
from services.main_logic import filtering_by_date
from statistics_m.utils import PurchaseListAndAddMixin


class StatisticsListAndAdd(PurchaseListAndAddMixin, View):
    """Отображение Формы, Статистики и Фильтра в одном шаблоне"""

    form = PurchaseAddForm
    queryset = filtering_by_date
    template_name = 'statistics/statistics.html'
