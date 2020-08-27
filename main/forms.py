from django import forms
from main.models import Type, Purchase


class PurchaseAddForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['type', 'cost']