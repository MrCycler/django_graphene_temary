from django.db import models

# Create your models here.
#*Question model:
class Question(models.Model):
    #*Enunciado
    description = models.CharField("enunciado de la pregunta",max_length=500, blank=True)
    #*Imagen de enunciado
    image = models.ImageField("imagen del enunciado",upload_to='questions/%Y/%m/%d/',blank=True)
    #*Puntaje de la pregunta
    score = models.IntegerField("puntaje de pregunta",blank=False,default=1)
    #*Es una pregunta de ejemplo
    is_example = models.BooleanField("pregunta de ejemplo",blank=False,default=False)
    #Campos de creación y modificación
    created_at = models.DateTimeField("fecha de creación",auto_now_add=True)
    modified_at = models.DateTimeField("fecha de edición",auto_now=True)
    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"
    def __str__(self):
        return "Pregunta: ("+str(self.id)+") "

#*Opciones de pregunta:
class QuestionOptions(models.Model):
    #*Las opciones pertenecen a una pregunta
    question = models.ForeignKey(Question,verbose_name='pregunta', related_name='options', on_delete=models.CASCADE,null=True, blank=True)
    #*Enunciado
    text = models.CharField("texto de la opción",max_length=500, blank=True)
    #*Imagen de opcion de pregunta
    image = models.ImageField("imagen de la opción",upload_to='questions_options/%Y/%m/%d/',blank=True)
    #*Es una respuesta correcta
    is_correct = models.BooleanField("es correcta",blank=False,default=False)
    #Campos de creación y modificación
    created_at = models.DateTimeField("fecha de creación",auto_now_add=True)
    modified_at = models.DateTimeField("fecha de edición",auto_now=True)
    class Meta:
        verbose_name = "Opcion de pregunta"
        verbose_name_plural = "Opciones de pregunta"
    def __str__(self):
        return "Opcion de pregunta: ("+str(self.id)+") "