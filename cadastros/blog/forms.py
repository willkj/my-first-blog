from django import forms
from . models import *

class UsuarioForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ["codigo","endereco","numero","cidade","estado","datanasc","cpf","rg","nome", "email", "sexo",]
