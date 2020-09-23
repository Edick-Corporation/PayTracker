from django.shortcuts import redirect
from datetime import datetime
from main.models import Purchase, Type
from services.main_logic import get_users_purchases


def _get_purchases_of_week(self):
    """Сервис для получения номеров недель"""

    date_purchase = get_users_purchases(self).values_list('date', flat=True)
    week_list = []
    for i in date_purchase:
        week_list.append(datetime.isocalendar(i)[1])
    clear_weeks = list(set(week_list))
    clear_weeks = sorted(clear_weeks)
    return clear_weeks


def _cost_values_of_purchases(self):
    """Сервис для получения покупок по заданым неделям"""

    purchases = []
    for weeks in _get_purchases_of_week(self):
        purchases.append(get_users_purchases(self).filter(date__week=weeks).values_list('cost', flat=True))
    return purchases


def _count_weeks(self):
    """Сервис для получения количества недель"""

    return len(_cost_values_of_purchases(self))


def _expenses_by_every_week(self):
    """Сервис для получения трат по заданным неделям"""

    expenses_by_every_week = []
    for num in range(0, _count_weeks(self)):
        expenses_by_every_week.append(sum(_cost_values_of_purchases(self)[num]))
    return expenses_by_every_week


def count_average_expenses_by_week(self):
    """Сервис для получения среднего числа трат по неделям"""

    dirty_average = float((sum(_expenses_by_every_week(self))) / _count_weeks(self))
    dirty_average = round(dirty_average, 2)
    ready_average = str(dirty_average).split()
    return ready_average