from django import forms
from main.models import Purchase


class PurchaseAddForm(forms.ModelForm):
    """Модель формы для записи покупок"""
    class Meta:
        model = Purchase
        fields = ['type', 'cost', ]