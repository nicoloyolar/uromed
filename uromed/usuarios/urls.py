from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('agenda/', agenda_view, name='agenda_view'),  
    path('detalle_paciente/', detalle_paciente_view, name='detalle_paciente'),
    path('informes/', informes_view, name='informes_view'),  
    path('nuevo_paciente/', nuevo_paciente_view, name='nuevo_paciente'), 
    path('examenes/', examenes_view, name='examenes_view'), 
    path('lista_examenes/', lista_examenes_view, name='lista_examenes'),
    path('lista_pacientes/', lista_pacientes_view, name='lista_pacientes'),
    path('paciente/<int:paciente_id>/', nuevo_o_actualizar_paciente, name='nuevo_o_actualizar_paciente'),
    path('paciente/', nuevo_o_actualizar_paciente, name='nuevo_o_actualizar_paciente'),
    path('eliminar_paciente/<int:id>/', eliminar_paciente_view, name='eliminar_paciente'),

]
