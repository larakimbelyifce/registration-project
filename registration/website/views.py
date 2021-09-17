# Utilizando a ListView para a listagem de funcionários.
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from registration.models import Funcionario
from django.urls import reverse_lazy

# Create your views here.
class FuncionarioListView(ListView):
    template_name = 'website/lista.html'
    model = Funcionario
    context_object_name = 'funcionarios'

class FuncionarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    models = Funcionario
    fields = '__all__'
    context_object_name = 'funcionario'

    # Busca de objeto utilizando o método get_object() da classe pai UpdateView.
    def get_object(self, queryset = None):
        funcionario = None

        # Os campos {pk} e {slug} estão presentes em self.kwargs.
        id = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
            # Busca de funcionário a partir do id.
            funcionario = Funcionario.objects.filter(id = id).first()

        elif slug is not None:
            # Pega o campo slug do Model.
            campo_slug = self.get_slug_field()

            # Busca o funcionário a partir do slug.
            funcionario = Funcionario.objects.filter(**{campo_slug: slug}).first()

            # Retorna o objeto encontrado
            return funcionario

class FuncionarioDeleteView(DeleteView):
    template_name = 'website/exclui.html'
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy(
        'website:lista_funcionarios'
    )

class FuncionarioCreateView(CreateView):
    template_name = 'website/cria.html'
    model = Funcionario
    form_class = InsereFuncionarioForm

    # O método reverse_lazy() traduz a View em URL.
    success_url = reverse_lazy(
        'website:lista_funcionarios'
    )
