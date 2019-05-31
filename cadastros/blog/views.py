from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.
def cadastrar_usuario(request):
    form = UsuarioForm()
    return render(request,  'blog/form.html',{'form':form})
