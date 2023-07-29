from django import forms
from .models import Vehiculo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Formulario_ingreso(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class RegistroUsuario(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
        

