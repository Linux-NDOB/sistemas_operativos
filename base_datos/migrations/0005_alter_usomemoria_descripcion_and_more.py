# Generated by Django 4.0.5 on 2022-06-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_datos', '0004_alter_usomemoria_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usomemoria',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usomemoria',
            name='usuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]