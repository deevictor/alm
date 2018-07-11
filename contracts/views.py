from django.shortcuts import render

from .forms import ContractForm
from .models import Contract
from .filters import ContractFilter
from django.db.models.functions import TruncMonth, TruncDay

# Create your views here.

def contract_list(request):
    contract_list = Contract.objects.all()
    contract_filter = ContractFilter(request.GET, queryset=contract_list)

    context = {
        "contract_list": contract_list,
        "filter": contract_filter,
        "title": "Contract List"
    }
    return render(request, "contract_list.html", context)