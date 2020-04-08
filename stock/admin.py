from django.contrib import admin
from .models import Stock


class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'description', 'presentation', 'quantity')


admin.site.register(Stock, StockAdmin)
