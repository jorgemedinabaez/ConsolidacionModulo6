from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import Formulario_ingreso,RegistroUsuario
from .models import Vehiculo
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.

def index_view(request):
    return render(request,'vehiculo/index.html')

@login_required(login_url='/login/')
@permission_required(perm='can_add_vehiculo',login_url='/login/')
def registro_view(request):
    if request.method == 'POST':
        form = Formulario_ingreso(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registrado satisfactoriamente")
        return redirect('registro')
    else:
        form = Formulario_ingreso()
    return render(request,'vehiculo/formulario.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f'iniciaste sesión como: {username}.')
                return HttpResponseRedirect('/')
            else:
                messages.error(request,'username y/o password incorrecto')
                return HttpResponseRedirect('/login')
        else:
            messages.error(request,'username y/o password incorrecto')
            return HttpResponseRedirect('/login')

    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request,'vehiculo/login.html',context)

def logout_view(request):
    logout(request)
    messages.info(request,'Se ha cerrado sesión exitosamente.')
    return HttpResponseRedirect('/')

@permission_required(perm='vehiculo.visualizar_catalogo',login_url='/login/')
def listar_view(request):
    vehiculos = Vehiculo.objects.all()
    context = {'vehiculos':vehiculos}
    return render(request,'vehiculo/listar.html',context)

def registroUsuario_view(request):
    if request.method =='POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(Vehiculo)
            visualizar_catalogo = Permission.objects.get(
                codename='visualizar_catalogo',
                content_type = content_type
            )
            user = form.save()
            user.user_permissions.add(visualizar_catalogo)
            login(request,user)
            messages.success(request,"Registrado satisfactoriamente.")
            return HttpResponseRedirect('/')
        messages.error(request,"Registro invalido. Algunos datos son incorrectos")
    form = RegistroUsuario()
    context = {'register_form':form}
    return render(request, "vehiculo/registro.html", context)