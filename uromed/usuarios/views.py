from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Examen, Paciente

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

def nuevo_paciente_view(request):
    return render(request, 'usuarios/nuevo_paciente.html')  

@login_required
def examenes_view(request):
    examenes = Examen.objects.all()
    return render(request, 'usuarios/lista_examenes.html', {'examenes': examenes})

@login_required
def lista_examenes_view(request):
    examenes = Examen.objects.all()
    return render(request, 'usuarios/lista_examenes.html', {'examenes': examenes})

@login_required
def lista_pacientes_view(request):
    pacientes = Paciente.objects.all()  
    return render(request, 'usuarios/lista_pacientes.html', {'pacientes': pacientes})

@login_required
def detalle_paciente_view(request):
    return render(request, 'usuarios/detalle_paciente.html')

def nuevo_o_actualizar_paciente(request, paciente_id=None):
    
    paciente = None
    if paciente_id:
        paciente = get_object_or_404(Paciente, pk=paciente_id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        edad = request.POST.get('edad')
        genero = request.POST.get('genero')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        estado_civil = request.POST.get('estado_civil')
        antecedentes_medicos = request.POST.get('antecedentes_medicos')
        alergias = request.POST.get('alergias')
        medicamentos = request.POST.get('medicamentos')
        presion_arterial = request.POST.get('presion_arterial')
        frecuencia_cardiaca = request.POST.get('frecuencia_cardiaca')
        peso = request.POST.get('peso')
        talla = request.POST.get('talla')
        saturacion = request.POST.get('saturacion')
        temperatura = request.POST.get('temperatura')
        frecuencia_respiratoria = request.POST.get('frecuencia_respiratoria')

        if paciente:
            paciente.nombre = nombre
            paciente.apellido = apellido
            paciente.edad = edad
            paciente.genero = genero
            paciente.direccion = direccion
            paciente.telefono = telefono
            paciente.email = email
            paciente.fecha_nacimiento = fecha_nacimiento
            paciente.estado_civil = estado_civil
            paciente.antecedentes_medicos = antecedentes_medicos
            paciente.alergias = alergias
            paciente.medicamentos = medicamentos
            paciente.presion_arterial = presion_arterial
            paciente.frecuencia_cardiaca = frecuencia_cardiaca
            paciente.peso = peso
            paciente.talla = talla
            paciente.saturacion = saturacion
            paciente.temperatura = temperatura
            paciente.frecuencia_respiratoria = frecuencia_respiratoria
            paciente.save()
        else:
            paciente = Paciente(
                nombre=nombre,
                apellido=apellido,
                edad=edad,
                genero=genero,
                direccion=direccion,
                telefono=telefono,
                email=email,
                fecha_nacimiento=fecha_nacimiento,
                estado_civil=estado_civil,
                antecedentes_medicos=antecedentes_medicos,
                alergias=alergias,
                medicamentos=medicamentos,
                presion_arterial=presion_arterial,
                frecuencia_cardiaca=frecuencia_cardiaca,
                peso=peso,
                talla=talla,
                saturacion=saturacion,
                temperatura=temperatura,
                frecuencia_respiratoria=frecuencia_respiratoria
            )
            paciente.save()

        return redirect('lista_pacientes')

    return render(request, 'nuevo_paciente.html', {'paciente': paciente})