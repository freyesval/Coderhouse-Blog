from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *
from django.views.generic.list import ListView

class CreateForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = ['titulo', 'subtitulo', 'contenido', 'autor','imagen', 'etiqueta', 'estado']

class PageEditForm(forms.ModelForm):
    class Meta:
        model = Pages
        fields = ['titulo', 'subtitulo', 'contenido','imagen']
