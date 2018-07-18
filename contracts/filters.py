from django import forms
from django.contrib.postgres.forms import RangeWidget 
# from django_filters import RangeWidget
from .models import Contract, Company, Contract_type, Currency

import django_filters

class ContractFilter(django_filters.FilterSet):
    company = django_filters.ModelMultipleChoiceFilter(queryset=Company.objects.all(), widget=forms.CheckboxSelectMultiple)
    contract_type = django_filters.ModelMultipleChoiceFilter(queryset=Contract_type.objects.all(), widget=forms.CheckboxSelectMultiple)
    currency_type = django_filters.ModelMultipleChoiceFilter(queryset=Currency.objects.all(), widget=forms.CheckboxSelectMultiple)
    # year_range = django_filters.DateFromToRangeFilter(base_widget=RangeWidget(attrs={'placehoder': 'YYY/MM/DD'}), queryset=Contract.objects.all())
    date_end = django_filters.NumberFilter(name= 'date_end', lookup_expr='year')
    date_range= django_filters.DateRangeFilter(name='')

    class Meta:
        model = Contract
        fields = ['company', 'contract_type', 'currency_type', 'date_start', 'date_end', 'contract_value']

# class ContractFilterMonthly(ContractFilter):
#         time = django_filters.

#     class Meta:
#         fields = ['company', 'contract_type', 'currency_type', 'date_start', 'date_end', 'contract_value']