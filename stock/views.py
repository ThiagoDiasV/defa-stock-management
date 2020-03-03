from django.shortcuts import render, reverse, redirect
from .forms import StockCategoryForm
from .models import Stock
from django.core import serializers
from django.http import HttpResponse


def stock(request):
    form = StockCategoryForm()
    return render(request, "stock/stock.html", {"form": form})


def query_category(category):
    queryset = Stock.objects.filter(category=category)
    return queryset


def category(request):
    category = request.GET['category']
    queryset = query_category(category)
    json_data = serializers.serialize("json", queryset)
    return HttpResponse(json_data)
