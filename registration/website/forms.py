from registration.models import Funcionario
from django import forms

# Formulário de inserção usando ModelForm.
class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
        # Modelo que o Django deve pegar os campos.
        model = Funcionario
        # Os campos que estarão no formulário serão apresentados através do atributo fields.
        fields = [
            'nome',
            'email',
            'cpf',
            'celular',
            'rg',
            'endereco',
            'salario'
        ]

        # Caso queira remover algum campo do formulário, basta adicionálo ao exclude.
        # exclude = ['salario']

        # Caso queira adicionar outros campos, independente dos campos do Model.
        # chefe = forms.BooleanField(label='Chefe?',  required=False)
        # biografia = forms.CharField(label='Biografia', required=False, widget=forms.Textarea)
