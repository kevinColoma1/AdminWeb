# Generated by Django 3.2.7 on 2021-11-06 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0008_alter_cargo_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='empleado',
            table='empleados_empleado',
        ),
    ]
