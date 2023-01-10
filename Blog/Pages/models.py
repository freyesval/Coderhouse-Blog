from django.db import models
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe

ESTADO = (
    (0,"Draft"),
    (1,"Publish")
)

class Pages(models.Model):
    titulo=models.CharField(max_length=50)
    etiqueta = models.SlugField(default="",max_length=200, unique=False)
    subtitulo=models.CharField(max_length=150)
    contenido = RichTextField()
    def html_content(self):
        return mark_safe(self.contenido)
    autor=models.ForeignKey(User,on_delete=models.CASCADE)
    fecha=models.DateField(auto_now_add=True)
    estado = models.IntegerField(choices=ESTADO, default=0)
    imagen=models.ImageField(upload_to='pages_img',default='default.png',blank=True)

    class Meta:
        ordering=['-fecha']
    
    @property
    def get_image(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url
        else:
            return "/media/pages_img/default.png"

    def __str__(self):
        return f"Autor: {self.autor} - Título: {self.titulo} - Fecha: {self.fecha}"