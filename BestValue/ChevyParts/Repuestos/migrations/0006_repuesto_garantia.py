# Generated by Django 3.2.7 on 2021-12-23 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Repuestos', '0005_repuesto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='repuesto',
            name='Garantia',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], default='0', max_length=1),
        ),
    ]
