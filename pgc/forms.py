from django import forms
from .models import PgcProduct

# from django.db.utils import ProgrammingError


class PgcItemCategoryForm(forms.Form):
    list_name = forms.ModelChoiceField(
        queryset=PgcProduct.objects.values_list("list_name", flat=True)
        .distinct("list_name")
        .filter(is_opened_to_order=True)
    )
