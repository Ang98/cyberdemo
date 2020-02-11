from django.db import models

# Create your models here.


class PartidoPolitico(models.Model):


    #atributos propios de partido politico
    nombre = models.CharField(max_length=45, blank=True, default='')
    estado = models.CharField(max_length=45, blank=True, default='')

    # atributos de auditoria
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=45, blank=True, default='')


class EsegJNE(models.Model):

    #atributos propios de eseg_jne
    estado = models.IntegerField()
    dni_responsable = models.CharField(max_length=45, blank=True, default='')
    apellidos = models.CharField(max_length=100, blank=True, default='')
    nombres = models.CharField(max_length=100, blank=True, default='')
    sugerencia = models.CharField(max_length=400, blank=True, default='')
    observacion = models.CharField(max_length=400, blank=True, default='')

    # atributos de auditoria
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=45, blank=True, default='')



class PlanEstudio(models.Model):
    # atributos foraneos
    id_seg = models.ForeignKey(EsegJNE, on_delete=models.CASCADE)

    #atributos propios de plan de estudio
    nombre = models.CharField(max_length=100, blank=True, default='')
    estado = models.CharField(max_length=45,blank=True,default='')

    # atributos de auditoria
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=45, blank=True, default='')

class SecretariaPP(models.Model):
    # atributos foraneos
    id_partido = models.ForeignKey(PartidoPolitico, on_delete=models.CASCADE)

    #atributos propios de secretaria partido politico
    nombre = models.CharField(max_length=45,blank=True,default='')
    descripcion = models.CharField(max_length=200, blank=True, default='')
    responsable = models.CharField(max_length=45, blank=True, default='')

    # atributos de auditoria
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=45, blank=True, default='')


class Militante(models.Model):

    #atributos foraneos militante
    id_militante = models.ForeignKey('self', on_delete=models.CASCADE)
    id_plan = models.ForeignKey(PlanEstudio, on_delete=models.CASCADE)
    id_partido = models.ForeignKey(PartidoPolitico, on_delete=models.CASCADE)

    #atributos propios de militante
    dni = models.CharField(max_length=15,blank=True,default='')
    apellidos = models.CharField(max_length=100,blank=True,default='')
    nombres = models.CharField(max_length=100,blank=True,default='')
    perfil = models.CharField(max_length=45, blank=True, default='')
    cargo = models.CharField(max_length=45, blank=True,default='')

    # atributos de auditoria
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=45, blank=True, default='')


class Examen(models.Model):


    #atributos propios de examen
    tipo = models.CharField(max_length=45, blank=True, default='')
    responsable = models.CharField(max_length=45, blank=True, default='')

    # atributos de auditoria
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=45, blank=True, default='')


class MilitanteExamen(models.Model):

    # atributos foraneos
    id_militante= models.ForeignKey(Militante, on_delete=models.CASCADE)
    id_examen = models.ForeignKey(Examen, on_delete=models.CASCADE)

    #atributos propios de militante_examen
    nota = models.IntegerField()

    # atributos de auditoria
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=45, blank=True, default='')

class Pregunta(models.Model):

    #atributos propios de pregunta
    contenido = models.CharField(max_length=600, blank=True, default='')

    # atributos de auditoria
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=45, blank=True, default='')


class ExamenPregunta(models.Model):

    # atributos foraneos
    id_examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    # atributos propios de examen_pregunta

    # no tiene

    # atributos de auditoria
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=45, blank=True, default='')


class Debate(models.Model):
    # atributos foraneos
    id_militante = models.ForeignKey(Militante, on_delete=models.CASCADE)

    #atributos propios de debate
    tema = models.CharField(max_length=45, blank=True, default='')
    estado = models.CharField(max_length=45, blank=True, default='')
    moderador = models.CharField(max_length=45, blank=True, default='')

    # atributos de auditoria
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=45, blank=True, default='')


class Usuario(models.Model):

    # atributos foraneos
    id_militante = models.ForeignKey(Militante, on_delete=models.CASCADE)

    #atributos propios de usuario
    usuario = models.CharField(max_length=45, blank=True, default='')
    contra = models.CharField(max_length=45, blank=True, default='')

    # atributos de auditoria
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=45, blank=True, default='')

class Curso(models.Model):

    # atributos foraneos
    id_plan = models.ForeignKey(PlanEstudio, on_delete=models.CASCADE)

    #atributos propios de curso
    nombre_curso = models.CharField(max_length=45, blank=True, default='')
    sumilla = models.CharField(max_length=300, blank=True, default='')
    docente = models.CharField(max_length=100, blank=True, default='')

    # atributos de auditoria
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=45, blank=True, default='')


class Conferencia(models.Model):

    #atributos foraneos
    id_plan = models.ForeignKey(PlanEstudio,on_delete=models.CASCADE)

    #atributos propios de conferencia
    tema = models.CharField(max_length=45, blank=True, default='')
    apellidos_conferencista = models.CharField(max_length=100, blank=True, default='')
    nombres_conferecista = models.CharField(max_length=100, blank=True, default='')
    tipo = models.CharField(max_length=45, blank=True, default='')

    #atributos de auditoria
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_registro = models.CharField(max_length=45, blank=True, default='')
    fecha_modificacion = models.DateField(auto_now=True)
    usuario_modificacion = models.CharField(max_length=45, blank=True, default='')