from django.contrib import admin

# Register your models here.
from .models import Contract, Company, Contract_type, Currency

class ContractAdmin(admin.ModelAdmin):
    list_display = ["id", "company", "contract_type", "currency_type", "date_start", "date_end", "contract_value"]
    list_display_links = ["id"]
    list_editable = ["company", "contract_type", "currency_type", "date_start", "date_end", "contract_value"]
    list_filter = ["company", "contract_type", "currency_type", "date_start", "date_end", "contract_value"]

    search_fields = ["company", "contract_type", "currency_type", "date_start", "date_end", "contract_value"]

    # class Meta:
    #     model = Contract

admin.site.register(Contract, ContractAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id"]
    list_editable = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]

    class Meta:
        verbose_name_plural = "companies"

admin.site.register(Company, CompanyAdmin)


class Contract_typeAdmin(admin.ModelAdmin):
    list_display = ["id", "contract_type"]
    list_display_links = ["id"]
    list_editable = ["contract_type"]
    list_filter = ["contract_type"]
    search_fields = ["contract_type"]

admin.site.register(Contract_type, Contract_typeAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ["id", "currency_type"]
    list_display_links = ["id"]
    list_editable = ["currency_type"]
    list_filter = ["currency_type"]
    search_fields = ["currency_type"]

    class Meta:
        verbose_name_plural = "companies"

admin.site.register(Currency, CurrencyAdmin)