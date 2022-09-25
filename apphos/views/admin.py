from django.contrib import admin
from apphos.models.Auxiliar import Auxiliar
from apphos.models.Enfermero import Enfermero
from apphos.models.Familiar import Familiar
from apphos.models.Historia_clinica import Historia_clinica
from apphos.models.Login import login
from apphos.models.Medico import Medico
from apphos.models.Paciente import Paciente
from apphos.models.Signos_vitales import Signos_vitales


admin.site.register(Auxiliar)
admin.site.register(Enfermero)
admin.site.register(Familiar)
admin.site.register(Historia_clinica)
admin.site.register(login)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Signos_vitales)




