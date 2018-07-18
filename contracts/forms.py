from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Contract, Company, Contract_type, Currency

class SearchForm(forms.Form):
    company= forms.ModelMultipleChoiceField(queryset=Company.objects.all(), widget=forms.CheckboxSelectMultiple, label="Компания")
    contract_type= forms.ModelMultipleChoiceField(queryset=Contract_type.objects.all(), widget=forms.CheckboxSelectMultiple, label="Тип договора")
    currency_type= forms.ModelMultipleChoiceField(queryset=Currency.objects.all(), widget=forms.CheckboxSelectMultiple, label="Тип валюты")
    selected_year = forms.IntegerField(required=False, label="Год")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

