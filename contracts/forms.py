from django import forms

from .models import Contract, Company, Contract_type, Currency

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            "company",
            "contract_type",
            "currency_type",
            "date_start",
            "date_end",
            "contract_value"
        ]

class Company(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name"]

class Contract_type(forms.ModelForm):
    class Meta:
        model = Contract_type
        fields = ["contract_type"]

class Currency(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ["currency_type"]