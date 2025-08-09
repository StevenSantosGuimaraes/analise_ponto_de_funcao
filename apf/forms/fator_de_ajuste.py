from django import forms

from apf.models import FatorAjuste


class FatorAjusteForm(forms.ModelForm):

    class Meta:
        model = FatorAjuste
        fields = [
            'comunicacao_dados',
            'processamento_distribuido',
            'desempenho',
            'configuracao_equipamento',
            'volume_transacoes',
            'entrada_dados_online',
            'eficiencia_usuario_final',
            'atualizacao_online',
            'processamento_complexo',
            'reusabilidade',
            'facilidade_instalacao',
            'facilidade_operacao',
            'multiplos_locais',
            'facilidade_mudanca',
        ]
        widgets = {field: forms.NumberInput(attrs={'min': 0, 'max': 5}) for field in fields}
