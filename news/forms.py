from django import forms
# from .models import Usuario, Publicacion
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'password']


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['comentario', 'usuario']

