from django.shortcuts import render, redirect
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaForm
from .models import Post

def home(request):
    return render(request, "blog/home.html")

def agregar_autor(request):
    form = AutorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, "blog/form.html", {'form': form, 'titulo': 'Agregar Autor'})

def agregar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, "blog/form.html", {'form': form, 'titulo': 'Agregar Categoría'})

def agregar_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, "blog/form.html", {'form': form, 'titulo': 'Agregar Post'})

def buscar_post(request):
    resultados = []
    if request.GET.get('titulo'):
        form = BusquedaForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaForm()
    return render(request, "blog/buscar.html", {'form': form, 'resultados': resultados})

from django.shortcuts import render

def about_view(request):
    return render(request, 'blog/about.html')