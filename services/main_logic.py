from django.shortcuts import redirect
from main.models import Purchase, Type


def get_users_purchases(self):
    """Севрис для фильтрации Покупок по Юзерам"""
    try:
        return Purchase.objects.filter(user=self.request.user.profile.pk)
    except AttributeError:
        print('hi')


def get_users_purchases_by_type(self):
    """Сервис для фильтрации Покупок по Типам"""
    return Purchase.objects.filter(user=self.request.user.profile.pk, type__slug=self.kwargs['type_slug'])


def get_type_list():
    """Сервис для получения всех Типов"""
    return Type.objects.all()