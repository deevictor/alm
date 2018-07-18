from django.shortcuts import render
import datetime, calendar
from django.db.models import Count, Sum, Q
from django.db.models.functions import TruncMonth, TruncDay, ExtractWeek

from .forms import ContractForm
from .models import Contract
from .filters import ContractFilter


# Create your views here.

def contract_list(request):
    contract_list = Contract.objects.all()

    contract_list_monthly = Contract.objects.annotate(month=TruncMonth('date_end')).values('company_id', 'contract_type', 'currency_type','month').annotate(summed_value=Sum('contract_value')).order_by()

    # contract_list_daily = Contract.objects.annotate(day=TruncDay('date_end')).values('day').annotate(summed_value=Sum('contract_value')).order_by()

    # print(contract_list_monthly)
    # print(contract_list_daily)
    # print(contract_list)

    contract_filter = ContractFilter(request.GET, queryset=contract_list)

    contract_filter_monthly = contract_filter.qs.annotate(month=TruncMonth('date_end')).values('company__name', 'contract_type__contract_type', 'currency_type__currency_type','month').annotate(summed_value=Sum('contract_value')).order_by()

    contract_filter_weekly = contract_filter.qs.annotate(month=TruncMonth('date_end'), week=ExtractWeek('date_end')).values('company__name', 'contract_type__contract_type', 'currency_type__currency_type','month').annotate(summed_value=Sum('contract_value')).order_by()


    # print(contract_list.filter(pk__in=[]))
    print(contract_filter_monthly)

    if request.method == "GET":
        qd = request.GET
        date_year = int(qd.get('date_end'))
        month_total_value_dict = {}
        for month_number in range(1, 13):
            month_name = calendar.month_name[month_number]
            month_first_date = datetime.date(date_year, month_number, 1)
            month_last_date = datetime.date(date_year, month_number, calendar.monthrange(date_year, month_number)[1])
            month_contractobj_qs = contract_filter.qs.filter(date_start__lte=month_last_date, date_end__lte=month_first_date)
            month_total_value_dict[month_name] = month_contractobj_qs.aggregate(monthly_value=Sum('contract_value'))

    context = {
        "contract_list": contract_list,
        "filter_monthly": contract_filter_monthly,
        "month_total_value_dict": month_total_value_dict,
        "filter_weekly": contract_filter_weekly,
        "filter": contract_filter,
        "title": "Contract List"
    }
    return render(request, "contract_list.html", context)

