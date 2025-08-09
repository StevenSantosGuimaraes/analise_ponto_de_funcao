from django.db import models


class Linguagem(models.Model):
    
    nome = models.CharField(max_length=50, unique=True)
    produtividade = models.FloatField(help_text="Pontos de Função por dia")
    custo_hora = models.FloatField(help_text="Custo por hora (R$)")

    class Meta:
        db_table = 'linguagens'
        verbose_name = 'Linguagem'
        verbose_name_plural = 'Linguagens'

    def __str__(self):
        return self.nome
