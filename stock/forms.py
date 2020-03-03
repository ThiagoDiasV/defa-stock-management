from django import forms
from .models import Stock
from django.db.utils import ProgrammingError


class StockCategoryForm(forms.Form):
    try:
        queryset = Stock.objects.values_list("category", flat=True).distinct()
        queryset_choices = [("", "Selecione uma categoria")] + [(id, id) for id in queryset]
        category = forms.ChoiceField(
            label="Categoria", choices=queryset_choices, widget=forms.Select()
        )

    except ProgrammingError:
        pass
