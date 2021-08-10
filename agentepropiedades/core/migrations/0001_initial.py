# Generated by Django 3.1.7 on 2021-08-10 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombreCliente', models.CharField(max_length=10)),
                ('primerApellido', models.CharField(max_length=20)),
                ('segundoApellido', models.CharField(max_length=20)),
                ('direccion', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=15)),
                ('operacion', models.CharField(max_length=15)),
                ('superficie', models.IntegerField()),
                ('habitaciones', models.IntegerField()),
                ('banno', models.IntegerField()),
                ('ubicacion', models.TextField()),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('imgane', models.ImageField(null=True, upload_to='propiedades')),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_galeria', models.FileField(null=True, upload_to='Propiedades')),
                ('propiedad', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.propiedad')),
            ],
        ),
    ]
