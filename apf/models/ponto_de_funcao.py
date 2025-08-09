from django.db import models

from .projeto import Projeto


class PontoFuncao(models.Model):

    TIPOS_COMPONENTE = (
        ('EE', 'Entrada Externa'),
        ('SE', 'Saída Externa'),
        ('CE', 'Consulta Externa'),
        ('ALI', 'Arquivo Lógico Interno'),
        ('AIE', 'Arquivo de Interface Externa'),
    )

    COMPLEXIDADES = (
        ('LOW', 'Baixa'),
        ('MEDIUM', 'Média'),
        ('HIGH', 'Alta'),
    )

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    tipo_componente = models.CharField(max_length=3, choices=TIPOS_COMPONENTE)
    complexidade = models.CharField(max_length=10, choices=COMPLEXIDADES)
    quantidade = models.PositiveIntegerField(default=1)
    descricao = models.CharField(max_length=255, blank=True, help_text="Descrição do componente ou referência.")

    class Meta:
        db_table = 'pontos_funcao'
        verbose_name = 'Ponto de Função'
        verbose_name_plural = 'Pontos de Função'

    def calcular_pontos(self):
        pesos = {
            'EE': {'LOW': 3, 'MEDIUM': 4, 'HIGH': 6},
            'SE': {'LOW': 4, 'MEDIUM': 5, 'HIGH': 7},
            'CE': {'LOW': 3, 'MEDIUM': 4, 'HIGH': 6},
            'ALI': {'LOW': 7, 'MEDIUM': 10, 'HIGH': 15},
            'AIE': {'LOW': 5, 'MEDIUM': 7, 'HIGH': 10},
        }
        return pesos[self.tipo_componente][self.complexidade] * self.quantidade
