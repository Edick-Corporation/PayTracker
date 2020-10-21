import datetime

from django.shortcuts import redirect

from services.main_logic import get_users_purchases



def _get_purchase_date(self):
    """Сервис для получение дат покупок"""

    date_purchase = get_users_purchases(self).values_list('date', flat=True)
    return date_purchase


def _weeks_datetime_to_str(self):
    """Сервис для обработки и изменения формата дат"""

    dirty_date_of_weeks = []
    for i in _get_purchase_date(self):
        start_week = i - datetime.timedelta(i.weekday())
        end_week = start_week + datetime.timedelta(7)
        s_w = datetime.datetime.strftime(start_week, '%Y-%m-%d')
        e_w = datetime.datetime.strftime(end_week, '%Y-%m-%d')

        dirty_date_of_weeks.append(s_w + ' ' + e_w)
    return dirty_date_of_weeks


def _remove_duplicates(self):
    """Сервис для обнаружения и удаления дубликатов"""

    clear_date_of_weeks = list(set(_weeks_datetime_to_str(self)))
    return clear_date_of_weeks


def _get_sorted_date(self):
    """Сервис для сортировки дат по возрастанию"""

    sorted_date_of_weeks = sorted(_remove_duplicates(self))
    return sorted_date_of_weeks


def _get_ready_date_of_weeks(self):
    """Сервис для подготовтки дат для date__range в формат ['start_week', 'end_week']"""

    ready_date_of_weeks = []
    for dates in _get_sorted_date(self):
        ready_date_of_weeks.append(dates.split())
    return ready_date_of_weeks


def _cost_values_of_purchases(self):
    """Сервис для получения покупок по заданым датам"""

    purchases = []
    for weeks in _get_ready_date_of_weeks(self):
        purchases.append(get_users_purchases(self).filter(date__range=weeks).values_list('cost', flat=True))
    return purchases


def _count_weeks(self):
    """Сервис для получения количества недель"""

    return len(_cost_values_of_purchases(self))


def _expenses_by_every_week(self):
    """Сервис для получения трат по заданым датам"""

    expenses_by_every_week = []
    for num in range(0, _count_weeks(self)):
        expenses_by_every_week.append(sum(_cost_values_of_purchases(self)[num]))
    return expenses_by_every_week


def _get_dirty_average(self):
    """Сервис для получения грязного среднего значение"""

    dirty_average = float((sum(_expenses_by_every_week(self))) / _count_weeks(self))
    dirty_average = round(dirty_average, 2)
    return dirty_average


def get_ready_average(self):
    """Сервис для изменения формата на строку"""
    try:
        ready_average = str(_get_dirty_average(self)).split()
        return ready_average
    except ZeroDivisionError:
        return ['0']



