from django.contrib import admin
from .models import Withdrawal
from django.utils import timezone


def local_date(obj):
    local_date = timezone.localtime(obj.date)
    printable_date = local_date.strftime("%m/%d/%Y - %H:%M:%S")
    return printable_date


class WithdrawalAdmin(admin.ModelAdmin):
    list_display = (local_date, "client", "sector", "product", "quantity")
    list_display_links = (local_date, )
    list_filter = ('client', 'sector', 'product')
    # search_fields = ('client', 'sector', 'product')


admin.site.register(Withdrawal, WithdrawalAdmin)
