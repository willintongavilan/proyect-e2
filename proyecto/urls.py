"""proyecto URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from apphos import views


urlpatterns = [
    path('login/', views.createloginview.as_view()),
    path('Enfermero/', views.createenfermeroview.as_view()),   
    path('Medico/', views.createmedicoview.as_view()),
    path('Auxiliar/', views.createauxiliarview.as_view()),
    path('Familiar/', views.createfamiliarview.as_view()),
    path('Historia_clinica/', views.createhistoriaclinicaview.as_view()),
    path('Paciente/', views.createpacienteview.as_view()),
    path('Signos_vitales/', views.createsignosvitalesview.as_view()),
   

    path('login/<int:pk>/', views.detailloginview.as_view()),
    path('Auxiliar/<int:pk>/', views.detailauxiliarview.as_view()),
    path('Familiar/<int:pk>/', views.detailfamiliarview.as_view()),
    path('Historia_clinica/<int:pk>/', views.detailhistoriaclinicaview.as_view()),
    path('Signos_vitales/<int:pk>/', views.detailsignosvitalessview.as_view()),
    path('Paciente/<int:pk>/', views.detailpacienteview.as_view()),
    path('Medico/<int:pk>/', views.detailmedicoview.as_view()),
    path('Enfermero/<int:pk>/', views.detailenfermeroview.as_view()),
    


    ]
#127.0.0.1:8000/api/Paciente

