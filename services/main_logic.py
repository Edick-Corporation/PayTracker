from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import datetime

from statistics_m.forms import PurchaseAddForm
from main.models import Purchase, Type


def user_is_anonymous(obj):
    """Сервис для проверки Пользователя"""
    try:
        return obj
    except AttributeError:
        return HttpResponseRedirect('accounts/login/')


def get_users_purchases(self):
    """Севрис для фильтрации Покупок по Юзерам"""
    users_purchases = Purchase.objects.filter(user=self.request.user.profile.pk)
    return user_is_anonymous(obj=users_purchases)


def get_type_list():
    """Сервис для получения всех Типов"""
    return Type.objects.all()


def _is_valid(value):
    """Проверка на пустое поле"""

    return value != '' and value is not None


def filter_statistics_by_date_and_types(self):
    """Сервис календарь для фильтрации Покупок по дате и Типу"""
    qs = get_users_purchases(self)
    type_of_purchase = self.request.GET.get('type')
    date_min = self.request.GET.get('date_min')
    date_max = self.request.GET.get('date_max')

    if _is_valid(type_of_purchase) and type_of_purchase != 'All':
        qs = qs.filter(type__slug=type_of_purchase)

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
        form = PurchaseAddForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.user = request.user.profile
            purchase.save()
            return redirect('pie-chart')


def get_filtered_qs_by_date(self):
    qs = get_users_purchases(self)

    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)

    value_month = date.month
    value_year = date.year

    week = self.request.GET.get('week')
    month = self.request.GET.get('month')
    year = self.request.GET.get('year')

    if _is_valid(week):
        qs = qs.filter(date__range=[start_week, end_week])

    if _is_valid(month):
        qs = qs.filter(date__month=value_month)

    if _is_valid(year):
        qs = qs.filter(date__year=value_year)
    return qs


def get_name_of_types(self):
    user_types = get_filtered_qs_by_date(self).values_list('type', flat=True)
    clear_types = list(set(user_types))
    name_of_types = list(Type.objects.filter(id__in=clear_types).values_list('name', flat=True))
    print(name_of_types)
    if name_of_types is None:
        return ['No recorded purchases']
    else:
        return name_of_types


def prices(self):
    dirty_prices = []
    for t in get_name_of_types(self):
        dirty_prices.append(get_filtered_qs_by_date(self).filter(type__name=t).values_list('cost', flat=True))
    clear_prices = []
    for d_p in dirty_prices:
        clear_prices.append(list(d_p))
    return clear_prices


def count_prices_per_type(self):
    list_counted = []
    for p in prices(self):
        list_counted.append(sum(p))
    return list_counted


def get_ready_data_of_prices(self):
    ready_data = []
    for prices_of_types in count_prices_per_type(self):
        ready_data.append(float(prices_of_types))
    print('price', ready_data)
    if ready_data is []:
        return [0]
    else:
        return ready_data