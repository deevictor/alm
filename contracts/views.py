from django.shortcuts import render
import datetime, calendar, json
from django.db.models import Count, Sum, Q
from django.db.models.functions import TruncMonth, TruncDay, ExtractWeek
from django.utils import translation
from django.utils.translation import ugettext as _
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from .forms import SearchForm
from .models import Contract

# Create your views here.

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
        # print(monthly_contract_dict)
        # monthly_contract_dict_js = serializers.serialize("json", monthly_contract_dict)

    form = SearchForm(request.GET or None)
    context = {
        "title": "Контракты",
        "form": form,
        "contract_list": contract_list,
        "monthly_contract_dict": monthly_contract_dict,
        # "monthly_contract_dict_js": monthly_contract_dict_js,
        "monthly_contract_dict_total": monthly_contract_dict_total
    }

    return render(request, "contract_list.html", context)

def get_contracts(request):
    if request.method == 'GET':
        selected_year = request.GET.get('selected_year', None)
        selected_month = request.GET.get('selected_month', None)
        # print(name)
        # data = {}
        # data['returned_name'] = name
        data = {
            'selected_year': selected_year,
            'selected_month': selected_month,
            'added_attr': "bla bla bla"
        }

    # return HttpResponse(json.dumps(data), content_type="application/json")
    return JsonResponse(data)