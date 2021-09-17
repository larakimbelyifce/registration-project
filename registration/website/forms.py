from registration.registration.models import Funcionario
from django import forms
from django.forms import fields

# Criação dos campos do form usando ModelFrom.
class InsereFuncionarioForm(forms.ModelForm):
    class Meta:
        # Modelo base.
        model = Funcionario
        # Campos que estarão no form.
        fields = [
            'nome',
            'email',
            'cpf',
            'celular',
            'rg',
            'endereco',
            'salario'
        ]
