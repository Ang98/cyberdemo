from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

#PRUEBA
router.register('users',UserViewSet)


#CYBERDEMOCRACIA
router.register('pp',PartidoPoliticoViewset)
router.register('eseg',EsegJNEViewSet)
router.register('plan',PlanEstudioViewSet)
router.register('secretaria',SecretariaPPViewSet)
router.register('militante',MilitanteViewSet)
router.register('examen',ExamenViewSet)
router.register('militanteExamen',MilitanteExamenViewSet)
router.register('pregunta',PreguntaViewSet)
router.register('examenPregunta',ExamenPreguntaViewSet)
router.register('debate',DebateViewSet)
router.register('usuario',UsuarioViewSet)
router.register('curso',CursoViewSet)
router.register('conferencia',ConferenciaViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
