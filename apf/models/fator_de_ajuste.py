from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apf.models.projeto import Projeto


class FatorAjuste(models.Model):

    projeto = models.OneToOneField(
        Projeto,
        on_delete=models.CASCADE,
        related_name="fatores_ajuste"
    )

    validators = [MinValueValidator(0), MaxValueValidator(5)]

    comunicacao_dados = models.IntegerField(default=0, validators=validators)
    processamento_distribuido = models.IntegerField(default=0, validators=validators)
    desempenho = models.IntegerField(default=0, validators=validators)
    configuracao_equipamento = models.IntegerField(default=0, validators=validators)
    volume_transacoes = models.IntegerField(default=0, validators=validators)
    entrada_dados_online = models.IntegerField(default=0, validators=validators)
    eficiencia_usuario_final = models.IntegerField(default=0, validators=validators)
    atualizacao_online = models.IntegerField(default=0, validators=validators)
    processamento_complexo = models.IntegerField(default=0, validators=validators)
    reusabilidade = models.IntegerField(default=0, validators=validators)
    facilidade_instalacao = models.IntegerField(default=0, validators=validators)
    facilidade_operacao = models.IntegerField(default=0, validators=validators)
    multiplos_locais = models.IntegerField(default=0, validators=validators)
    facilidade_mudanca = models.IntegerField(default=0, validators=validators)
    
    class Meta:
        db_table = 'fatores_ajuste'
        verbose_name = 'Fator de Ajuste'
        verbose_name_plural = 'Fatores de Ajuste'

    def calcular_fit(self):
        """Calcula o Fator de Influência Total (FIT) somando todos os campos."""
        fit = sum([
            self.comunicacao_dados, self.processamento_distribuido, self.desempenho,
            self.configuracao_equipamento, self.volume_transacoes, self.entrada_dados_online,
            self.eficiencia_usuario_final, self.atualizacao_online, self.processamento_complexo,
            self.reusabilidade, self.facilidade_instalacao, self.facilidade_operacao,
            self.multiplos_locais, self.facilidade_mudanca
        ])
        return fit
