# Generated by Django 3.2.7 on 2021-12-22 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedores', '0002_auto_20211221_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='Ruc',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='Teléfono',
            field=models.CharField(max_length=10),
        ),
    ]
