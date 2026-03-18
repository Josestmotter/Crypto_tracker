from django.db import models

class PrecoMoeda(models.Model):
    moeda = models.CharField(max_length=10)
    preco = models.DecimalField(max_digits=20, decimal_places=8)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.moeda} - {self.preco} - {self.criado_em}"