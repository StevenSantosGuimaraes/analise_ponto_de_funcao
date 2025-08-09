from django import forms

from apf.models import Projeto


class ProjetoForm(forms.ModelForm):

    class Meta:
        model = Projeto
        fields = ['nome', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }
