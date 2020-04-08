from django.db import models


class PgcProduct(models.Model):
    list_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=200)
    has_catmat = models.BooleanField()
    catmat = models.CharField(max_length=6)
    ref_number = models.CharField(max_length=8)
    unit = models.CharField(max_length=6)
    is_opened_to_order = models.BooleanField(default=False)
