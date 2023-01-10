from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import *
from .forms import *
from Accounts.models import Profile
from Accounts.views import *


def home(request):
    return render(request, 'Pages/pages_list.html')

def about(request):
    return render(request, 'Pages/about.html')

class PagesListView(ListView):
    queryset = Pages.objects.filter(estado=1).order_by('fecha')
    model= Pages
    template_name="Pages/pages_list.htmml"

def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            titulo = form.cleaned_data.get("titulo")
            subtitulo = form.cleaned_data.get("subtitulo")
            contenido = form.cleaned_data.get("contenido")
            autor = form.cleaned_data.get("autor")
            imagen = form.cleaned_data.get("imagen")
            etiqueta = form.cleaned_data.get("etiqueta")
            estado = form.cleaned_data.get("estado")
            post= Pages(
                titulo=titulo, 
                subtitulo=subtitulo,
                contenido=contenido,
                autor=autor,
                imagen=imagen,
                etiqueta=etiqueta,
                estado=estado)
            post.save()
            return redirect("home")
    else:
        form = CreateForm()
    return render(request, "Pages/createpage.html", {"form": form})

def editpage(request, etiqueta):
    edit_page = Pages.objects.get(etiqueta=etiqueta)
    if request.method == "POST":
        form = PageEditForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            edit_page.titulo = data["titulo"]
            edit_page.subtitulo=data["subtitulo"]
            edit_page.contenido =data["contenido"]
            edit_page.imagen =data["imagen"]
            edit_page.save()
            return redirect('home')
        else:
            form = PageEditForm()
            return render(request,"Pages/editpage.html",{"etiqueta": etiqueta, "form": form})
    else:
        form = PageEditForm(
            initial={
                "titulo": edit_page.titulo,
                "subtitulo": edit_page.subtitulo,
                "contenido": edit_page.contenido,
                "imagen": edit_page.imagen,
            }
        )
        return render(request,"Pages/editpage.html",{"etiqueta": etiqueta, "form": form})

def page_detail(request, etiqueta):
    page = Pages.objects.filter(etiqueta=etiqueta)

    return render(request, "Pages/page_detail.html", {"page": page})

def deletepage(request, etiqueta):
    page=Pages.objects.filter(etiqueta=etiqueta)
    page.delete()
    return redirect("home")