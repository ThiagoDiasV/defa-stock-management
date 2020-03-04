from django import forms
from .models import Stock
from django.db.utils import ProgrammingError


class StockCategoryForm(forms.Form):
    try:
        queryset = Stock.objects.values_list("category", flat=True).distinct()
        queryset_choices = [("Todos", "Listar tudo")] + [(id, id) for id in queryset]
        category = forms.ChoiceField(
            label="Categoria", choices=queryset_choices, widget=forms.Select()
        )

    except ProgrammingError:
        category = forms.ChoiceField(
            label="Categoria", widget=forms.Select()
        )
