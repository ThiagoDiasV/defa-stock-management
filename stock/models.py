from django.db import models


class Stock(models.Model):

    category_choices = [
        ("Reagentes e correlatos", "Reagentes e correlatos"),
        ("EPIs", "EPIs"),
        ("Correlatos em geral", "Correlatos em geral"),
        ("Meios de Cultura", "Meios de Cultura"),
        ("Antibiograma", "Antibiograma"),
        ("Ativos Farmacêuticos", "Ativos Farmacêuticos")
    ]

    category = models.CharField(max_length=50, choices=category_choices)
    description = models.CharField(max_length=300)
    presentation = models.CharField(max_length=40)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.description}"

    class Meta:
        ordering = ['category']
