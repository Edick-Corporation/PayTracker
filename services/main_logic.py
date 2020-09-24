from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
import datetime

from statistics_m.forms import PurchaseAddForm
from main.models import Purchase, Type


def user_is_anonymous(obj):
    """Сервис для проверки Пользователя"""
    try:
        return obj
    except AttributeError:
        return redirect('account_login')


def get_users_purchases(self):
    """Севрис для фильтрации Покупок по Юзерам"""
    return Purchase.objects.filter(user=self.request.user.profile.pk)


def get_type_list():
    """Сервис для получения всех Типов"""

    return Type.objects.all()


def _is_valid(value):
    """Проверка на пустое поле"""

    return value != '' and value is not None


def filter_statistics_by_date_and_types(self):
    """Сервис календарь для фильтрации Покупок по дате и Типу"""

    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)

    value_month = date.month
    value_year = date.year

    qs = get_users_purchases(self)
    types = get_type_list()

    type_of_purchase = self.request.GET.get('type')

    week = self.request.GET.get('week')
    month = self.request.GET.get('month')
    year = self.request.GET.get('year')

    date_min = self.request.GET.get('date_min')
    date_max = self.request.GET.get('date_max')

    if _is_valid(date_min):
        qs = qs.filter(date__gte=date_min)

    if _is_valid(date_max):
        qs = qs.filter(date__lt=date_max)
        print(type(date_min), type(date_max))

    if _is_valid(type_of_purchase) and type_of_purchase != 'All':
        qs = qs.filter(type__slug=type_of_purchase)

    if _is_valid(week):
        qs = qs.filter(date__range=[start_week, end_week])

    if _is_valid(month):
        qs = qs.filter(date__month=value_month)

    if _is_valid(year):
        qs = qs.filter(date__year=value_year)

    return qs


def get_form_to_record_purchase():
    """Сервис для получении формы"""

    form = PurchaseAddForm()
    return form


def add_purchase(self, request):
    """Сервис для ПОСТ запроса с Формы"""

    if self.request.method == 'POST':
        form = PurchaseAddForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user.profile
            purchase.save()
            return redirect('statistics')