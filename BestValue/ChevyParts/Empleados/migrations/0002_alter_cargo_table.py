# Generated by Django 3.2.7 on 2021-11-06 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cargo',
            table='empleados_cargo',
        ),
    ]