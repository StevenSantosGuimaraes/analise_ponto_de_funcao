import logging

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apf.forms import (
    FatorAjusteForm,
    ProjetoForm,
    PontoFuncaoForm
)
from apf.models import Projeto
from apf.models.linguagem import Linguagem


logger = logging.getLogger('apf')


class ProjetoListView(ListView):
    
    model = Projeto
    template_name = 'projeto/lista.html'


class ProjetoCreateView(CreateView):

    model = Projeto
    form_class = ProjetoForm
    template_name = 'projeto/formulario.html'
    success_url = reverse_lazy('project_list')


class ProjetoUpdateView(UpdateView):
    model = Projeto
    form_class = ProjetoForm
    template_name = 'projeto/formulario.html'
    success_url = reverse_lazy('project_list')


class ProjetoDeleteView(DeleteView):
    model = Projeto
    template_name = 'projeto/confirmar_exclusao.html'
    success_url = reverse_lazy('project_list')


class ProjetoDetailView(DetailView):

    model = Projeto
    template_name = 'projeto/detalhe.html'

    def get_context_data(self, **kwargs):
        componentes_do_projeto = self.object.pontofuncao_set.all()
        context = super().get_context_data(**kwargs)
        context['componentes'] = componentes_do_projeto
        context['ponto_funcao_form'] = PontoFuncaoForm()
        context['fator_ajuste_form'] = FatorAjusteForm()

        linguagens = Linguagem.objects.all()
        context['linguagens'] = linguagens

        linguagem_id = self.request.GET.get('linguagem')
        linguagem_selecionada = None
        estimativa = None

        if componentes_do_projeto.exists():
            try:
                context['pfna'] = self.object.calcular_pfna()
                context['vaf'] = self.object.calcular_vaf()
                context['pf_ajustado'] = self.object.calcular_pf_ajustado()

                if linguagem_id:
                    try:
                        linguagem_selecionada = Linguagem.objects.get(id=linguagem_id)
                        pf_ajustado = context['pf_ajustado']
                        dias = pf_ajustado / linguagem_selecionada.produtividade if linguagem_selecionada.produtividade else 0
                        horas = dias * 8
                        custo = horas * linguagem_selecionada.custo_hora
                        estimativa = {
                            'linguagem': linguagem_selecionada,
                            'dias': dias,
                            'horas': horas,
                            'custo': custo
                        }
                    except Linguagem.DoesNotExist:
                        pass
            except Exception as e:
                logger.error(f"Erro ao calcular PF para projeto {self.object.id}: {str(e)}")
                context['erro'] = "Erro ao calcular Pontos de Função."
        else:
            context['erro'] = "Dados insuficientes para calcular Pontos de Função."

        context['linguagem_selecionada'] = linguagem_selecionada
        context['estimativa'] = estimativa
        return context
    