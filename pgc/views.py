from django.shortcuts import render
from .forms import PgcItemCategoryForm
from .models import PgcProduct
from django.core import serializers
from django.http import HttpResponse


def pgc(request):
    form = PgcItemCategoryForm()
    return render(request, "pgc/pgc.html", {"form": form})


def list_name(request):
    list_name = request.GET["list_name"]
    queryset = PgcProduct.objects.filter(list_name=list_name)
    json_data = serializers.serialize("json", queryset)
    return HttpResponse(json_data)
