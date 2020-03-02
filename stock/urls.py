from django.urls import path
from .views import stock, category_view

urlpatterns = [
    path("", stock, name="stock"),
    path("category/", category_view, name="category_view"),
]
