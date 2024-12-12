from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('detalle_paciente/<int:paciente_id>/', detalle_paciente_view, name='detalle_paciente'),
    path('eliminar_paciente/<int:id>/', eliminar_paciente_view, name='eliminar_paciente'),
    path('nuevo_paciente/', nuevo_paciente_view, name='nuevo_paciente'),
    path('paciente/<int:paciente_id>/', nuevo_o_actualizar_paciente, name='nuevo_o_actualizar_paciente'),
    path('paciente/', nuevo_o_actualizar_paciente, name='nuevo_o_actualizar_paciente'),
]
