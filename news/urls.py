from django.urls import path
from .views import index, index_admin

urlpatterns = [
    path("", index, name="news_index"),
    path("administrador/", index_admin, name="admin_index"),
    
]
