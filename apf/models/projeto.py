from django.db import models



class Projeto(models.Model):

    nome = models.CharField(
        max_length=100
    )
    descricao = models.TextField(
        blank=True
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = 'projetos'
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.nome

    def calcular_pfna(self):
        return sum(componente.calcular_pontos() for componente in self.pontofuncao_set.all())

    def calcular_vaf(self):
        try:
            ajuste = self.fatores_ajuste
            total_caracteristicas = sum([
                ajuste.comunicacao_dados,
                ajuste.processamento_distribuido,
                ajuste.desempenho,
                ajuste.configuracao_equipamento,
                ajuste.volume_transacoes,
                ajuste.entrada_dados_online,
                ajuste.eficiencia_usuario_final,
                ajuste.atualizacao_online,
                ajuste.processamento_complexo,
                ajuste.reusabilidade,
                ajuste.facilidade_instalacao,
                ajuste.facilidade_operacao,
                ajuste.multiplos_locais,
                ajuste.facilidade_mudanca
            ])
            return 0.65 + (0.01 * total_caracteristicas)
        except Exception:
            return 1.0

    def calcular_pf_ajustado(self):
        return self.calcular_pfna() * self.calcular_vaf()
    