# Generated by Django 4.0.5 on 2022-06-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_datos', '0002_usocpu_cant_procesos_usocpu_nombre_catalogo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usomemoria',
            name='pid',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]