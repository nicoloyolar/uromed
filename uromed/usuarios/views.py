from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Por favor, completa todos los campos.')
            return render(request, 'usuarios/login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión con éxito.')
            return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)  
    return redirect('login')

def home_view(request):
    return render(request, 'usuarios/home.html')

def agenda_view(request):
    return render(request, 'usuarios/agenda.html')  

def informes_view(request):
    return render(request, 'usuarios/informes.html') 

def pacientes_view(request):
    return render(request, 'usuarios/pacientes.html')  

def examenes_view(request):
    return render(request, 'usuarios/examenes.html') 