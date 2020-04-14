from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

#from .views import PartidoPoliticoViewset
from .views import *


router = routers.DefaultRouter()


# CYBERDEMOCRACIA
router.register('pp', PartidoPoliticoViewSet)
router.register('eseg', EsegJNEViewSet)
router.register('plan', PlanEstudioViewSet)
router.register('secretaria', SecretariaPPViewSet)
router.register('persona', PersonaViewSet)
router.register('externo', ExternoViewSet)
router.register('administrador', AdministradorViewSet)
router.register('militante', MilitanteViewSet)
router.register('examen', ExamenViewSet)
router.register('militanteExamen', MilitanteExamenViewSet)
router.register('pregunta', PreguntaViewSet)
router.register('alternativa', AlternativaViewSet)
router.register('examenPregunta', ExamenPreguntaViewSet)
router.register('debate', DebateViewSet)
router.register('curso', CursoViewSet)
router.register('conferencia', ConferenciaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
