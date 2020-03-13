from django.db import models
from stock.models import Stock
from django.utils import timezone


class Withdrawal(models.Model):

    client = models.CharField(max_length=50)
    sector = models.CharField(max_length=80)
    product = models.ForeignKey(Stock, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        product_instance = Stock.objects.get(pk=self.product.id)
        if (
            product_instance.quantity > 0
            and product_instance.quantity - self.quantity >= 0
        ):
            product_instance.quantity -= self.quantity
            product_instance.save()
        else:
            raise Exception(
                "This product cannot be withdrawn. This quantity isn't available on stock"
            )

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        product_instance = Stock.objects.get(pk=self.product.id)
        product_instance.quantity += self.quantity
        product_instance.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        local_date = timezone.localtime(self.date)
        printable_date = local_date.strftime("%m/%d/%Y - %H:%M:%S")
        return f"{printable_date} / {self.client} / {self.product} / {self.quantity} units"

    class Meta:
        ordering = ["date"]
