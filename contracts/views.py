from django.shortcuts import render

from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth, TruncDay

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


    print(contract_list.filter(pk__in=[1, 2, 3]))
    # print(contract_filter_monthly.qs)

    # if request.method == "GET":
    #     qd = request.GET
    #     company_id = qd.getlist('company')
    #     contract_type_id = qd.getlist('contract_type')
    #     currency_type_id = qd.getlist('currency_type')
    #     # print(contract_type_id)
    #     for contract in contract_list_monthly:
    #         if contract




    context = {
        "contract_list": contract_list,
        "filter_monthly": contract_list_monthly,
        "filter": contract_filter,
        "title": "Contract List"
    }
    return render(request, "contract_list.html", context)

# <QuerySet [
#     {'day': datetime.date(2030, 5, 17), 's': Decimal('2000000.00')},
#     {'day': datetime.date(2020, 7, 15), 's': Decimal('5000000000.00')},
#     {'day': datetime.date(2020, 7, 14), 's': Decimal('41000000.00')},
#     {'day': datetime.date(2025, 10, 3), 's': Decimal('3125000.00')},
#     {'day': datetime.date(2020, 10, 8), 's': Decimal('1000000000.00')}]
# >