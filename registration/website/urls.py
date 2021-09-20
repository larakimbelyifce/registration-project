# Importação das funções definidas no arquivo views.py.
from django.urls import path
from website.views import IndexTemplateView, FuncionarioListView, FuncionarioUpdateView, FuncionarioDeleteView, FuncionarioCreateView

app_name = 'website'

# A urlpatterns contém a lista de roteamentos de URLs.
urlpatterns = [
    # GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /funcionarios
    path('funcionarios/', FuncionarioListView.as_view(), name="lista_funcionarios"),

    # Para atualizar o objeto, devemos buscá-lo via 'id' ou 'slug'. Também pode ser atualizado através do método get_object().
    # GET/POST /funcionario/{pk do objeto}
    path('funcionario/<pk>', FuncionarioUpdateView.as_view(), name = "atualiza_funcionario"),

    # Para deletar o objeto, o procedimento é parecido com o de atualização.
    # GET/POST /funcionario/excluir/{pk do objeto}
    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(), name="deleta_funcionario"),

    # GET /funcionario/cadastrar
    path('funcionario/cadastrar', FuncionarioCreateView.as_view(), name="cadastra_funcionario"),
]
