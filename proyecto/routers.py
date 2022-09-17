from apphos.viewsets import Pacienteviewsets
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Paciente',Pacienteviewsets)

#url/Paciente http://127.0.0.1:8000
