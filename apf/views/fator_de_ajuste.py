from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apf.forms import FatorAjusteForm
from apf.models import (
    FatorAjuste,
    Projeto
)


class FatorAjusteCreateView(CreateView):
    
    model = FatorAjuste
    form_class = FatorAjusteForm
    template_name = 'fator_ajuste/formulario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_id'] = self.kwargs['project_id']
        return context

    def form_valid(self, form):
        form.instance.projeto = Projeto.objects.get(pk=self.kwargs['project_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.kwargs['project_id']})


class FatorAjusteUpdateView(UpdateView):
    model = FatorAjuste
    form_class = FatorAjusteForm
    template_name = 'fator_ajuste/formulario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_id'] = self.object.projeto_id
        return context

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.projeto_id})


class FatorAjusteDeleteView(DeleteView):
    model = FatorAjuste
    template_name = 'fator_ajuste/confirmar_exclusao.html'

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.projeto_id})
    