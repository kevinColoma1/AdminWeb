# Generated by Django 3.2.7 on 2021-12-22 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedores', '0003_auto_20211222_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='Ruc',
            field=models.SlugField(max_length=13),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='Teléfono',
            field=models.SlugField(max_length=10),
        ),
    ]
