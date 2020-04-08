from django.contrib import admin
from pgc.models import PgcProduct


class PgcProductAdmin(admin.ModelAdmin):
    list_display = [
        "list_name",
        "product_description",
        "catmat",
        "ref_number",
        "unit",
        "is_opened_to_order",
    ]
    list_filter = ["is_opened_to_order", "list_name"]


admin.site.register(PgcProduct, PgcProductAdmin)
