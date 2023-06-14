from django.urls import path
from .views import index, index_admin, index_usuario

urlpatterns = [
    path("", index, name="index"),
    path("administrador/", index_admin, name="admin_index"),
    path("administrador/usuarios", index_usuario, name="usuario_index"),
    
]
