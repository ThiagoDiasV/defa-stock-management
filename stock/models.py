from django.db import models


class Stock(models.Model):

    category_choices = [
        ("REAGENTE", "Reagentes"),
        ("EPI", "EPI"),
        ("CORRELATO", "Correlatos"),
        ("MEIO DE CULTURA", "Meios de Cultura"),
        ("ANTIBIOGRAMA", "Antibiograma"),
    ]

    catmat = models.CharField(max_length=6, unique=True)
    category = models.CharField(max_length=50, choices=category_choices)
    description = models.CharField(max_length=300)
    presentation = models.CharField(max_length=20)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.catmat} - {self.description}"
