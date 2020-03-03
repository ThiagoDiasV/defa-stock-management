from django.urls import path
from .views import stock, category

urlpatterns = [
    path("", stock, name="stock"),
    path("category/", category, name="category"),
]
