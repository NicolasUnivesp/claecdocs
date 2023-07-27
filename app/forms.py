from django.forms import ModelForm
from app.models import Autores

class AutoresForm(ModelForm):
    class Meta:
        model = Autores
        fields = ['autor', 'contato', 'email', 'pais', 'estado', 'cidade', 'instituicao', 'curso', 'area', 'tema', 'titulo', 'trabalho', 'observacoes', 'data_inicio', 'data_entrega']