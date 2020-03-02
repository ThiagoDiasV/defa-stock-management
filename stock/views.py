from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .forms import StockCategoryForm
from .models import Stock


def stock(request):
    if request.method == "POST":
        form = StockCategoryForm(request.POST)

        if form.is_valid():
            category = form.data['category']
            queryset = query_category(category)
            return HttpResponseRedirect(reverse('category_view', queryset))
    else:
        form = StockCategoryForm()
    return render(request, "stock/stock.html", {"form": form})


def query_category(category):
    queryset = Stock.objects.filter(category=category)
    return queryset


def category_view(request, **kwargs):
    print(kwargs)
    return render(request, "stock/category.html")
