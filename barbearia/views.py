from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from barbearia.forms import CarrosForm
from barbearia.models import Carros

def home(request):
    data = {}
    data['db'] = Carros.objects.all()
    return render (request, 'index.html', data)            

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render (request, 'form.html', data)

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

def delete(request, pk, template_name='confirm.html'):
    post = get_object_or_404(Carros, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('home')
    return render(request, template_name, {'object':post})

def edit(request, pk, template_name='edit.html'):
    post = get_object_or_404(Carros, pk=pk)
    form = CarrosForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form':form})
  
