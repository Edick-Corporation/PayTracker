from django import forms
from main.models import Purchase
import datetime


class PurchaseAddForm(forms.ModelForm):
    """Модель формы для записи покупок"""

    class Meta:
        model = Purchase
        fields = ['type', 'cost']