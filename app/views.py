from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from app.models import Autores
from app.forms import AutoresForm

def home(request):
    data = {}
    data['db'] = Autores.objects.all()
    all = Autores.objects.all()
    paginator = Paginator(all, 2)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    search = request.GET.get('search')
    if search:
        data['db'] = Autores.objects.filter(autor__icontains=search)
    else:
        data['db'] = Autores.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form']= AutoresForm()
    return render(request, 'form.html', data)

def create(request):
    form = AutoresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Autores.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Autores.objects.get(pk=pk)
    data['form'] = AutoresForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data ={}
    data['db']=Autores.objects.get(pk=pk)
    form = AutoresForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save
        return redirect('home')

def delete(request, pk):
    db = Autores.objects.get(pk=pk)
    db.delete()
    return redirect('home')

