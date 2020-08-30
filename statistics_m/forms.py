from django import forms
from main.models import Purchase
import datetime


class PurchaseAddForm(forms.ModelForm):
    """Модель формы для записи покупок"""

    class Meta:
        model = Purchase
        fields = ['type', 'cost']


class PurchaseForWeek(forms.Form):
    start_of_week = forms.DateTimeField(widget=forms.HiddenInput, )
    end_of_week = forms.DateTimeField(widget=forms.HiddenInput)
