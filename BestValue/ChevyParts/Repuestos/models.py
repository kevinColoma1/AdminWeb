from django.db import models
from django.db.models.deletion import CASCADE
from Empleados.models import Empleado
from Proveedores.models import Proveedores

from Vehiculos.models import Vehiculo
from .choices import descripcion, garantia
# Create your models here.
class Repuesto(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre_repuesto = models.CharField(max_length=45)
    Marca = models.CharField(max_length=1, choices= descripcion, default='O')
    Vehiculo = models.ForeignKey(Vehiculo, null=True, blank=True, on_delete= models.CASCADE)
    Proveedor = models.ForeignKey(Proveedores, null = True, blank= True, on_delete=CASCADE)
    Precio = models.DecimalField(max_digits=8, decimal_places=2, default="")
    Imagen = models.ImageField(upload_to="Repuestos", null = True)
    Garantia = models.CharField(max_length=1, choices= garantia, default='0')
    
    
    