from django.contrib import admin
from apphos.models.Login import login

from apphos.models.Familiar import Familiar
from apphos.models.Medico import Medico
from apphos.models.Paciente import Paciente
from .models.Enfermero import Enfermero
from .models.Auxiliar import Auxiliar
from .models.Medico import Medico
from .models.Signos_vitales import Signos_vitales
from .models.Historia_clinica import Historia_clinica





# Register your models here.
admin.site.register(Enfermero)
admin.site.register(Auxiliar)
admin.site.register(Familiar)
admin.site.register(Historia_clinica)
admin.site.register(login)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Signos_vitales)
