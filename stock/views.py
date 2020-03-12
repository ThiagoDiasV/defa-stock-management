from django.shortcuts import render
from .forms import StockCategoryForm
from .models import Stock
from django.core import serializers
from django.http import HttpResponse


def stock(request):
    form = StockCategoryForm()
    return render(request, "stock/stock.html", {"form": form})


def category(request):
    category = request.GET["category"]
    if category == "Listar tudo":
        queryset = Stock.objects.filter(quantity__gt=0)
    else:
        queryset = Stock.objects.filter(category=category, quantity__gt=0)
    json_data = serializers.serialize("json", queryset)
    return HttpResponse(json_data)
