from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class Examen(models.Model):
    nombre          = models.CharField(max_length=100)
    descripcion     = models.TextField(blank=True, null=True)
    fecha           = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    PACIENTE = 'paciente'
    MEDICO = 'medico'
    ENFERMERO = 'enfermero'
    ADMINISTRADOR = 'administrador'
    
    ROL_CHOICES = [
        (PACIENTE, 'Paciente'),
        (MEDICO, 'Médico'),
        (ENFERMERO, 'Enfermero'),
        (ADMINISTRADOR, 'Administrador'),
    ]
    
    rol = models.CharField(
        max_length=13,  
        choices=ROL_CHOICES,
        default=PACIENTE,
    )

    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    historial_medico = models.TextField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_set', 
        blank=True,
        help_text='Grupos a los que pertenece este usuario.',
        verbose_name='grupos'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_set',  
        blank=True,
        help_text='Permisos específicos de este usuario.',
        verbose_name='permisos'
    )

    def __str__(self):
        return self.username

    def nombre_completo(self):
        return f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.username
