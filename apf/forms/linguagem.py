from django import forms
from apf.models.linguagem import Linguagem


class LinguagemForm(forms.ModelForm):

    class Meta:
        model = Linguagem
        fields = ['nome', 'produtividade', 'custo_hora']
