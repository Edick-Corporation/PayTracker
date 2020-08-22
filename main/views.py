from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
# fuck you
# СЛЫШ ты лучше успокой свой член лады?

from main.models import Purchase


class PurchaseList(ListView):
    model = Purchase
