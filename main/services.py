from django.shortcuts import redirect
from main.models import Purchase, Type


def get_users_purchases(self):
    try:
        return Purchase.objects.filter(user=self.request.user.profile.pk)
    except AttributeError:
        print('hi')


def get_users_purchases_by_type(self):
    return Purchase.objects.filter(user=self.request.user.profile.pk, type__slug=self.kwargs['type_slug'])


def get_type_list():
    return Type.objects.all()