from django.urls import path
from .views import pgc, list_name


urlpatterns = [
    path("", pgc, name="pgc"),
    path("list_name/", list_name, name="list_name"),
]
