from django.urls import path
from .views import pgc


urlpatterns = [path("", pgc, name="pgc")]
