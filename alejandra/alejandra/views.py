from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.models import User


from .forms import RegisterForm

from products.models import Product


def index(request):
    template_name = 'index.html'
    products = Product.objects.all().order_by('-pk')
    context = {
        'message': 'Listado de Productos',
        'products': products,
    }
    return render(request, template_name, context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    template_name = 'users/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])

            return redirect('index')
        else:
            messages.error(request, 'Usuario o Contraseña no validos')

    return render(request, template_name)


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    template_name = 'users/register.html'
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(
                request, f'El usuario {user.username} fue creado exitosamente')
            return redirect('index')

    return render(request, template_name, {
        'form': form,
    })
