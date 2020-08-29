from django.shortcuts import redirect
from django.utils import timezone
import datetime

from statistics_m.forms import PurchaseAddForm
from main.models import Purchase, Type


def user_is_anonymous(obj):
    """Сервис для проверки Пользователя"""

    try:
        return obj
    except AttributeError:
        return redirect('account_login')


def get_users_purchases(request):
    """Севрис для фильтрации Покупок по Юзерам"""
    return Purchase.objects.filter(user=request.user.profile.pk)


def get_users_purchases_by_type(self):
    """Сервис для фильтрации Покупок по Типам"""

    return get_users_purchases(self).filter(type__slug=self.kwargs['type_slug'])


def get_type_list():
    """Сервис для получения всех Типов"""

    return Type.objects.all()


def _is_valid(value):
    """Проверка на пустое поле"""

    return value != '' and value is not None


def shopping_filter_calendar(self):
    """Сервис календарь для фильтрации Покупок по дате"""

    qs = get_users_purchases(self.request)

    date_min = self.request.GET.get('date_min')
    date_max = self.request.GET.get('date_max')

    if _is_valid(date_min):
        qs = qs.filter(date__gte=date_min)

    if _is_valid(date_max):
        qs = qs.filter(date__lt=date_max)

    return qs


def get_form_to_record_purchase():
    """Сервис для получении формы"""

    form = PurchaseAddForm()
    return form


def add_purchase(self, request):
    """Сервис для ПОСТ запроса с Формы"""

    if self.request.method == 'POST':
        form = self.form(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user.profile
            purchase.save()
            return redirect('statistics')