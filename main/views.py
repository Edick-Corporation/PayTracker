from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView
import matplotlib.pyplot as plt
# Create your views here.
# fuck you
# СЛЫШ ты лучше успокой свой член лады?
from qsstats import QuerySetStats
from main.models import Purchase


class PurchaseList(ListView):
    model = Purchase
    template_name = 'purchase/list.html'

    def get_queryset(self):

        if self.request.user.is_anonymous:
            print('is_anonymous:')
        else:
            return Purchase.objects.filter(user__purchase=self.request.user.profile.pk)





