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
from django.views import View

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
                contract_list = contract_list.filter(**{lookup:attr_listid})
        # contract_list2 = contract_list.values(*attr_list).annotate(monthly_value=Sum('contract_value')).order_by('company')
        # print(contract_list2)

    monthly_contract_dict = {}
    monthly_contract_dict2 = {}
    monthly_contract_dict_js = {}
    monthly_contract_dict_total = {}
    json_dict = {}
    if qd.get('selected_year'):
        selected_year = int(qd.get('selected_year'))
        translation.activate('ru')
        for month_number in range(1, 13):
            month_name = _(calendar.month_name[month_number])
            month_first_date = datetime.date(selected_year, month_number, 1)
            month_last_date = datetime.date(selected_year, month_number, calendar.monthrange(selected_year, month_number)[1])
            month_contractobj_qs = contract_list.filter(date_start__lte=month_last_date, date_end__gte=month_first_date)
            monthly_contract_dict[month_name] = month_contractobj_qs
            # monthly_contract_dict2[month_name] = month_contractobj_qs

            monthly_contract_dict_total[month_name] = month_contractobj_qs.aggregate(monthly_value=Sum('contract_value'))
            monthly_contract_dict_js['month_id'+str(month_number)] = serializers.serialize("json", month_contractobj_qs, fields=('company', 'contract_type', 'currency_type', 'contract_value'), use_natural_foreign_keys=True)


        json_dict = json.dumps(monthly_contract_dict_js)
    # print(monthly_contract_dict_total)

    form = SearchForm(request.GET or None)
    context = {
        "title": "Контракты",
        "form": form,
        "contract_list": contract_list,
        "monthly_contract_dict": monthly_contract_dict,
        "json_dict": json_dict,
        "monthly_contract_dict_total": monthly_contract_dict_total
    }

    return render(request, "contract_list.html", context)
##################################################################
class Contract_listView(View):
    def get(self, request, *args, **kwargs):
        contract_list = Contract.objects.all()
        qd = request.GET
        attr_list = ['company', 'contract_type', 'currency_type']
        for attr in attr_list:
            if qd.get(attr):
                attr_listid = qd.getlist(attr)
                lookup = attr+'__in'
                contract_list = contract_list.filter(**{lookup:attr_listid})
        # contract_list2 = contract_list.values(*attr_list).annotate(monthly_value=Sum('contract_value')).order_by('company')
        # print(contract_list2)

        monthly_contract_dict = {}
        monthly_contract_dict2 = {}
        monthly_contract_dict_js = {}
        monthly_contract_dict_total = {}
        json_dict = {}
        if qd.get('selected_year'):
            selected_year = int(qd.get('selected_year'))
            translation.activate('ru')
            for month_number in range(1, 13):
                month_name = _(calendar.month_name[month_number])
                month_first_date = datetime.date(selected_year, month_number, 1)
                month_last_date = datetime.date(selected_year, month_number, calendar.monthrange(selected_year, month_number)[1])
                month_contractobj_qs = contract_list.filter(date_start__lte=month_last_date, date_end__gte=month_first_date)
                monthly_contract_dict[month_name] = month_contractobj_qs
                # monthly_contract_dict2[month_name] = month_contractobj_qs

                monthly_contract_dict_total[month_name] = month_contractobj_qs.aggregate(monthly_value=Sum('contract_value'))
                monthly_contract_dict_js['month_id'+str(month_number)] = serializers.serialize("json", month_contractobj_qs, fields=('company', 'contract_type', 'currency_type', 'contract_value'), use_natural_foreign_keys=True)


            json_dict = json.dumps(monthly_contract_dict_js)
        # print(monthly_contract_dict_total)
        form = SearchForm(request.GET or None)

        print(request.GET)
        context = {
            "title": "Контракты",
            "form": form,
            "contract_list": contract_list,
            "monthly_contract_dict": monthly_contract_dict,
            "json_dict": json_dict,
            "monthly_contract_dict_total": monthly_contract_dict_total
        }

        return render(request, "contract_list.html", context)