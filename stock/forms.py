from django import forms
from .models import Stock


class StockCategoryForm(forms.Form):
    queryset = Stock.objects.values_list("category", flat=True).distinct()
    queryset_choices = [("", "Selecione uma categoria")] + [(id, id) for id in queryset]
    category = forms.ChoiceField(
        label="Categoria", choices=queryset_choices, widget=forms.Select()
    )
