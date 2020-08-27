from django.views.generic import View

from main.models import Purchase
from main.forms import PurchaseAddForm
from main.utils import PurchaseListAndAddMixin


class PurchaseListAndAdd(PurchaseListAndAddMixin, View):
    """Представление для формы и модели в одном шаблоне"""

    form = PurchaseAddForm
    model = Purchase
    template_name = 'purchase/list.html'


