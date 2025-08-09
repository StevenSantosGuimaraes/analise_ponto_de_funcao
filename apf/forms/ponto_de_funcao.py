from django import forms

from apf.models import PontoFuncao


class PontoFuncaoForm(forms.ModelForm):

    class Meta:
        model = PontoFuncao
        fields = ['tipo_componente', 'complexidade', 'quantidade', 'descricao']
