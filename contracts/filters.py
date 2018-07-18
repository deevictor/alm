from django import forms
from django.contrib.postgres.forms import RangeWidget 
# from django_filters import RangeWidget
from .models import Contract, Company, Contract_type, Currency

import django_filters

class ContractFilter(django_filters.FilterSet):
    company = django_filters.ModelMultipleChoiceFilter(queryset=Company.objects.all(), widget=forms.CheckboxSelectMultiple)
    contract_type = django_filters.ModelMultipleChoiceFilter(queryset=Contract_type.objects.all(), widget=forms.CheckboxSelectMultiple)
    currency_type = django_filters.ModelMultipleChoiceFilter(queryset=Currency.objects.all(), widget=forms.CheckboxSelectMultiple)

    selected_year = django_filters.NumberFilter(name= 'date_end', lookup_expr='year')
    # date_range= django_filters.DateRangeFilter(name='')

    class Meta:
        model = Contract
        fields = ['company', 'contract_type', 'currency_type', 'date_start', 'selected_year', 'contract_value']
