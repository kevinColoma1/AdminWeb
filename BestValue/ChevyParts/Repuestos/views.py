from django.shortcuts import render, redirect
from .forms import RepuestoForm
from Repuestos.models import Repuesto
from Vehiculos.models import Vehiculo
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def repuesto(request):
    repuestos= Repuesto.objects.all()
    contexto = {
        'repuestos':repuestos
    }
    return render(request, 'index_repuesto.html', contexto)

@login_required
def crearRepuesto(request):
    if request.method == 'GET':
        form = RepuestoForm()
        contexto = {
            'form':form
        }
    else: 
        form = RepuestoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index_repuesto')
    return render(request, 'crear_repuesto.html', {'form':form})

@login_required
def editarRepuesto(request, id):
    repuestos = Repuesto.objects.get(id = id)
    if request.method == 'GET':
        form = RepuestoForm(instance=repuestos)
        contexto = {
            'form':form
        }
    else:
        form = RepuestoForm(request.POST, request.FILES, instance= repuestos)
        contexto={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index_repuesto')
    return render(request, 'editar_repuesto.html', contexto)


@login_required
def eliminarRepuesto(request, id):
    repuestos = Repuesto.objects.get(id = id)
    repuestos.delete()
    return redirect('index_repuesto')



from django.db import connection
def store_proc(request):
    try:
        cursor = connection.cursor()
        if request.method == 'POST':
            Marca = request.POST.get('marca')
            Modelo = request.POST.get('modelo')
            Año = request.POST.get('año')
            nombre_repuesto = request.POST.get('nombre_repuesto')
            cursor.callproc('valor', (Marca, Modelo, Año, nombre_repuesto))
            result = cursor.fetchall()
            return render(request, 'Buscar.html',{"result":result})
            
            
        else:
            Objeto = Repuesto.objects.raw('Select re.id ,ve.marca, ve.modelo, ve.año, re.Nombre_repuesto from vehiculos_vehiculo as ve inner join repuestos_repuesto as re on re.Vehiculo_id = ve.id') 
            return render(request, 'Buscar.html',{"Repuesto":Objeto})
    finally:
        cursor.close()
        
def reporte (request):
    Reporte = Repuesto.objects.filter(modelo__Precio__istartswith='').values('modelo')
    Reporte = Repuesto.objects.raw('Select ve.id, sum(Precio) as Total, ve.modelo from vehiculos_vehiculo as ve inner join repuestos_repuesto as re on re.Vehiculo_id = ve.id group by ve.modelo')
    return render (request, 'Reporte.html ', {"reporte": Reporte})

0