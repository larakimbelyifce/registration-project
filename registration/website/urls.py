# Importação da função index() definida no arquivo views.py.
from django.urls.conf import path
from . import views

# Definição do namespace do app website.
app_name = 'website'

# A urlpatterns contém a lista de roteamentos de URLs.
urlpatterns = [
    # Método GET /.
    path('', views.index, name='index'),
]
