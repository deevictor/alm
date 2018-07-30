from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Contract, Company, Contract_type, Currency
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SearchForm(forms.Form):
    company= forms.ModelMultipleChoiceField(
        queryset=Company.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Компания",
    )

    contract_type= forms.ModelMultipleChoiceField(
        queryset=Contract_type.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Тип договора",
        )

    currency_type= forms.ModelMultipleChoiceField(
        queryset=Currency.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Тип валюты",
    )

    selected_year = forms.IntegerField(
        required=False,
        min_value=1990,
        max_value=3000,
        label="Год",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-contrl',
                'id': 'year_id',
                'placeholder': 'выберите год..'
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-searchForm'
        self.helper.form_class ='blueForms'
        self.helper.form_method = 'get'
        self.helper.form_action = 'submit_search1'
        # self.helper.field_class = 'col-lg-8'
        self.helper.label_class = 'col-lg-2'

        self.helper.add_input(Submit('submit', 'Поиск'))

