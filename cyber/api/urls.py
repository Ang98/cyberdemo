"""Cyberdemocracia"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

#from .views import PartidoPoliticoViewset
from .views import *


router = routers.DefaultRouter()


# CYBERDEMOCRACIA
router.register('pp', PartidoPoliticoViewSet,basename='PartidoPolitico')
router.register('eseg', EsegJNEViewSet,basename='ESEG')
router.register('plan', PlanEstudioViewSet,basename='PlanEstudio')
router.register('secretaria', SecretariaPPViewSet,basename='Secretaria')
#router.register('persona', PersonaViewSet)
router.register('externo', ExternoViewSet,basename='Externo')
router.register('administrador', AdministradorViewSet,basename='Administrador')
router.register('militante', MilitanteViewSet,basename='Militante')
router.register('examen', ExamenViewSet,basename='Examen')
router.register('militanteExamen', MilitanteExamenViewSet,basename='MilitanteExamen')
router.register('pregunta', PreguntaViewSet,basename='Pregunta')
router.register('alternativa', AlternativaViewSet,basename='Alternativa')
router.register('examenPregunta', ExamenPreguntaViewSet,basename='ExamenPregunta')
router.register('debate', DebateViewSet,basename='Debate')
router.register('curso', CursoViewSet,basename='Curso')
router.register('conferencia', ConferenciaViewSet,basename='Conferencia')

#router.register('usr',UsuarioViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
