from django.shortcuts import render,redirect

# Create your views here.
from .models import Laptop
from .forms import LaptopForm

# Create your views here.
def laptopview(request):
    form = LaptopForm()
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_sh')
    template_name = 'Firstapp/laptop.html'
    context = {'form':form}
    return render(request,template_name,context)

def showlaptop(request):
    lap_obj = Laptop.objects.all()
    template_name = 'Firstapp/show.html'
    context = {'lap_obj':lap_obj}
    return render(request, template_name, context)

def deleteview(request,id):
    lap_obj = Laptop.objects.get(id=id)
    if request.method == 'POST':
        lap_obj.delete()
        return redirect('show_sh')
    template_name = 'Firstapp/delete.html'
    context = {'lap_obj':lap_obj}
    return render(request, template_name, context)

def updateview(request,id):
    lap_obj = Laptop.objects.get(id=id)
    form = LaptopForm(instance=lap_obj)
    if request.method == 'POST':
        form = LaptopForm(request.POST,instance=lap_obj)
        if form.is_valid():
            form.save()
            return redirect('show_sh')
    template_name = 'Firstapp/laptop.html'
    context = {'form':form}
    return render(request, template_name, context)
