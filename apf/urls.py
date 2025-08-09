from django.urls import path

from apf.views.projeto import (
    ProjetoListView, ProjetoCreateView, ProjetoDetailView,
    ProjetoUpdateView, ProjetoDeleteView
)
from apf.views.ponto_de_funcao import (
    PontoFuncaoCreateView, PontoFuncaoUpdateView, PontoFuncaoDeleteView
)

from apf.views.linguagem import (
    LinguagemListView, LinguagemCreateView, LinguagemUpdateView, LinguagemDeleteView
)
from apf.views.fator_de_ajuste import (
    FatorAjusteCreateView, FatorAjusteUpdateView, FatorAjusteDeleteView
)


urlpatterns = [

    path('', ProjetoListView.as_view(), name='project_list'),
    path('projeto/novo/', ProjetoCreateView.as_view(), name='project_create'),
    path('projeto/<int:pk>/', ProjetoDetailView.as_view(), name='project_detail'),
    path('projeto/<int:pk>/editar/', ProjetoUpdateView.as_view(), name='project_edit'),
    path('projeto/<int:pk>/remover/', ProjetoDeleteView.as_view(), name='project_delete'),

    path('componente/<int:pk>/editar/', PontoFuncaoUpdateView.as_view(), name='component_edit'),
    path('componente/<int:pk>/remover/', PontoFuncaoDeleteView.as_view(), name='component_delete'),
    path('projeto/<int:project_id>/componente/novo/', PontoFuncaoCreateView.as_view(), name='component_create'),

    path('ajuste/<int:pk>/editar/', FatorAjusteUpdateView.as_view(), name='adjustment_edit'),
    path('ajuste/<int:pk>/remover/', FatorAjusteDeleteView.as_view(), name='adjustment_delete'),
    path('projeto/<int:project_id>/ajuste/novo/', FatorAjusteCreateView.as_view(), name='adjustment_create'),

    path('linguagens/', LinguagemListView.as_view(), name='linguagem_list'),
    path('linguagens/nova/', LinguagemCreateView.as_view(), name='linguagem_create'),
    path('linguagens/<int:pk>/editar/', LinguagemUpdateView.as_view(), name='linguagem_edit'),
    path('linguagens/<int:pk>/remover/', LinguagemDeleteView.as_view(), name='linguagem_delete'),

]
