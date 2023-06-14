from django.shortcuts import render

from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def index_admin(request):
    return render(request, 'administrador/index.html')

def index_usuario(request):
    usuarios = Usuario.objects.all()
    context = { 'usuarios' : usuarios }

    # u = UsuarioForm(nombre='Benjamin', correo='benja@gmail.com', password="123123")
    # u.save()

    return render(request, 'administrador/usuario/index.html', context)