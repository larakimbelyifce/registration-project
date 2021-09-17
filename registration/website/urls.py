# Importação da função FuncionarioListView, definida no arquivo views.py.
from registration.registration.models import Funcionario
from registration.website.views import FuncionarioCreateView, FuncionarioDeleteView, FuncionarioListView
from django.urls.conf import path

# A urlpatterns contém a lista de roteamentos de URLs.
urlpatterns = [
    path(
        'funcionarios/',
        FuncionarioListView.as_view(),
        name='lista_funcionarios'
    ),
]

urlpatterns = [
    path(
        'funcionario/excluir/<pk>',
        FuncionarioDeleteView.as_view(),
        name='deleta_funcionario'
    ),
]

urlpatterns = [
    path(
        'funcionario/cadastrar/',
        FuncionarioCreateView.as_view(),
        name='cadastra_funcionario'
    ),
]
