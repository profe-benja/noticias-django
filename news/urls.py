from django.urls import path
from .views import index, index_admin, index_usuario, create_usuario, edit_usuario

urlpatterns = [
    path("", index, name="index"),
    path("administrador/", index_admin, name="admin_index"),
    path("administrador/usuarios", index_usuario, name="usuario_index"),
    path("administrador/usuarios/create", create_usuario, name="usuario_create"),
    path("administrador/usuarios/<int:id>/edit", edit_usuario, name="usuario_edit"),
    
]
