from django import forms
from .models import Stock
from django.db.utils import ProgrammingError


class StockCategoryForm(forms.Form):
    try:
        category = forms.ModelChoiceField(
            queryset=Stock.objects.values_list("category", flat=True).distinct("category"),
            empty_label="Listar tudo",
        )
    except ProgrammingError:
        category = forms.ChoiceField(label="Categoria", widget=forms.Select())
