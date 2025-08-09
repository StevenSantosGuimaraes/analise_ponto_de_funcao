from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apf.models.linguagem import Linguagem
from apf.forms.linguagem import LinguagemForm

class LinguagemListView(ListView):
    model = Linguagem
    template_name = 'linguagem/lista.html'

class LinguagemCreateView(CreateView):
    model = Linguagem
    form_class = LinguagemForm
    template_name = 'linguagem/formulario.html'
    success_url = reverse_lazy('linguagem_list')

class LinguagemUpdateView(UpdateView):
    model = Linguagem
    form_class = LinguagemForm
    template_name = 'linguagem/formulario.html'
    success_url = reverse_lazy('linguagem_list')

class LinguagemDeleteView(DeleteView):
    model = Linguagem
    template_name = 'linguagem/confirmar_exclusao.html'
    success_url = reverse_lazy('linguagem_list')
