from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_usuario, name='cadastrar_usuario'),

]
