from django.shortcuts import render
import datetime, calendar, json
from django.db.models import Count, Sum, Q
from django.db.models.functions import TruncMonth, TruncDay, ExtractWeek
from django.utils import translation
from django.utils.translation import ugettext as _
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers as r_serializers
from rest_framework.renderers import JSONRenderer

from .forms import SearchForm
from .models import Contract

# Create your views here.

class ContractSerializer(r_serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('company', 'contract_type', 'currency_type', 'contract_value')
        # depth = 1

def contract_list(request):
    contract_list = Contract.objects.all()
    if request.method == "GET":
        qd = request.GET
        attr_list = ['company', 'contract_type', 'currency_type']
        for attr in attr_list:
            if qd.get(attr):
                attr_listid = qd.getlist(attr)
                lookup = attr+'__in'
                contract_list = Contract.objects.filter(**{lookup:attr_listid})

    monthly_contract_dict = {}
    monthly_contract_dict_js = {}
    monthly_contract_dict_total = {}
    if qd.get('selected_year'):
        selected_year = int(qd.get('selected_year'))
        # print(selected_year)
        # for contract in contract_list:
        translation.activate('ru')
        for month_number in range(1, 13):
            month_name = _(calendar.month_name[month_number])
            month_first_date = datetime.date(selected_year, month_number, 1)
            month_last_date = datetime.date(selected_year, month_number, calendar.monthrange(selected_year, month_number)[1])
            month_contractobj_qs = contract_list.filter(date_start__lte=month_last_date, date_end__gte=month_first_date)
            monthly_contract_dict[month_name] = month_contractobj_qs

            monthly_contract_dict_total[month_name] = month_contractobj_qs.aggregate(monthly_value=Sum('contract_value'))
            # print(month_contractobj_qs)
            monthly_contract_dict_js['month_id'+str(month_number)] = serializers.serialize("json", month_contractobj_qs, fields=('company', 'contract_type', 'currency_type', 'contract_value'), use_natural_foreign_keys=True)

            # monthly_contract_dict_js[month_name] = month_contractobj_qs.values('company__name', 'contract_type__contract_type', 'currency_type__currency_type', 'contract_value')


            # py_list = ContractSerializer(month_contractobj_qs, many=True)
            # json_list = JSONRenderer().render(py_list.data)
            # monthly_contract_dict_js['month_id'+str(month_number)] = json_list


        # monthly_contract_dict_js = ContractSerializer()
        # monthly_contract_dict_js = JSONRenderer().render(monthly_contract_dict_js)
        json_dict = json.dumps(monthly_contract_dict_js)
        print(json_dict)

    form = SearchForm(request.GET or None)
    context = {
        "title": "Контракты",
        "form": form,
        "contract_list": contract_list,
        "monthly_contract_dict": monthly_contract_dict,
        "monthly_contract_dict_js": monthly_contract_dict_js,
        "json_dict": json_dict,
        "monthly_contract_dict_total": monthly_contract_dict_total
    }

    return render(request, "contract_list.html", context)

def get_contracts(request):
    if request.method == 'GET':
        selected_year = request.GET.get('selected_year', None)
        month_number = request.GET.get('selected_month', None)


        data = {
            'selected_year': selected_year,
            'selected_month': month_number,
        }

    return JsonResponse(data)