from django.shortcuts import render, redirect
from .models import AAticle
from .forms import AAticleForm

# Create your views here.

def index(request):
    atcs = AAticle.objects.all()
    
    context = {
        'atcs' : atcs,
    }
    
    return render(request, 'aaticles/index.html', context)

def detail(request, id):
    atc = AAticle.objects.get(id=id)

    context = {
        'atc' : atc,
    }

    return render(request, 'aaticles/detail.html', context)

def create(request):
    if request.method =='POST':
        form = AAticleForm(request.POST)

        if form.is_valid():
           atc = form.save()
           return redirect('aaticles:detail', id=atc.id)
    else:
        form = AAticleForm()
        
    context = {
        'form': form,
    }

    return render(request, 'aaticles/form.html', context)