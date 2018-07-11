from django import forms
from .models import Contract, Company, Contract_type, Currency

import django_filters

class ContractFilter(django_filters.FilterSet):
    company = django_filters.ModelMultipleChoiceFilter(queryset=Company.objects.all(), widget=forms.CheckboxSelectMultiple)
    contract_type = django_filters.ModelMultipleChoiceFilter(queryset=Contract_type.objects.all(), widget=forms.CheckboxSelectMultiple)
    currency_type = django_filters.ModelMultipleChoiceFilter(queryset=Currency.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Contract
        fields = ['company', 'contract_type', 'currency_type', 'date_start', 'date_end', 'contract_value']
