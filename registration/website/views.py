# Utilizando a ListView para a listagem de funcionários.
from registration.models import Funcionario
from django.views.generic import TemplateView, ListView

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'website/index.html'

class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = "funcionarios"
