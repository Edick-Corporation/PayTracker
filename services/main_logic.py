from django.shortcuts import redirect
from main.models import Purchase, Type


def get_users_purchases(self):
    """Севрис для фильтрации Покупок по Юзерам"""

    return Purchase.objects.filter(user=self.request.user.profile.pk)


def get_users_purchases_by_type(self):
    """Сервис для фильтрации Покупок по Типам"""

    return Purchase.objects.filter(user=self.request.user.profile.pk, type__slug=self.kwargs['type_slug'])


def get_type_list():
    """Сервис для получения всех Типов"""

    return Type.objects.all()


def _is_valid(value):
    """Проверка на пустое поле"""

    return value != '' and value is not None


def filtering_by_date(self):
    """Сервис для фильтрации Покупок по дате"""

    qs = get_users_purchases(self)
    date_min = self.request.GET.get('date_min')
    date_max = self.request.GET.get('date_max')

    if _is_valid(date_min):
        qs = qs.filter(date__gte=date_min)

    if _is_valid(date_max):
        qs = qs.filter(date__lt=date_max)

    return qs