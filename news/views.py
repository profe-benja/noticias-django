from django.shortcuts import render

from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def index_admin(request):
    return render(request, 'administrador/index.html')

def index_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        password = request.POST.get('pass')

        usuario = Usuario(nombre=nombre, password=password, email=correo)
        usuario.save()

    usuarios = Usuario.objects.all()
    context = { 'usuarios' : usuarios }
    return render(request, 'administrador/usuario/index.html', context)

def create_usuario(request):
     return render(request, 'administrador/usuario/create.html')