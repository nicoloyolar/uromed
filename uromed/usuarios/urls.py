from django.urls import path
from .views import login_view, logout_view, home_view, agenda_view, informes_view, nuevo_paciente_view, examenes_view

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('agenda/', agenda_view, name='agenda_view'),  
    path('informes/', informes_view, name='informes_view'),  
    path('nuevo_paciente/', nuevo_paciente_view, name='nuevo_paciente'), 
    path('examenes/', examenes_view, name='examenes_view'), 
]
