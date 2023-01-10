from django.contrib import admin
from .models import Pages

class PagesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'etiqueta', 'estado','fecha')
    list_filter = ("estado",)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'etiqueta': ('titulo',)}

admin.site.register(Pages, PagesAdmin)
