from registration.models import Funcionario
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# Utilizando a TemplateView para rederização da página.
class IndexTemplateView(TemplateView):
    template_name = "website/index.html"

# Utilizando a ListView para a listagem de funcionários.
class FuncionarioListView(ListView):
    template_name = "website/lista.html"
    model = Funcionario
    context_object_name = 'funcionarios'

# Utilizando a UpdateView para a atualização de funcionários.
class FuncionarioUpdateView(UpdateView):
    template_name = "website/atualiza.html"
    model = Funcionario
    fields = '__all__' # fields = ['nome', 'email', 'cpf', 'celular', 'rg', 'endereco', 'salario']
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionários")

# Utilizando a DeleteView para deletar um funcionário.
class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionarios")

# Utilizando a CreateView para adicionar um novo funcionário.
class FuncionarioCreateView (CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    # O método reverse_lazy() vai traduzir a View em URL. Após adicionar um funcionário, haverá um redirecionamento para a página de listagem atualizada.
    success_url = reverse_lazy("website:lista_funcionarios")