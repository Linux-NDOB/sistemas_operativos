# Generated by Django 4.0.5 on 2022-06-30 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_datos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usocpu',
            name='cant_procesos',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usocpu',
            name='nombre_catalogo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usomemoria',
            name='cant_procesos',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usomemoria',
            name='nombre_catalogo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
