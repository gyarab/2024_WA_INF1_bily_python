# Generated by Django 5.1.4 on 2025-02-21 11:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Castilla la Mancha', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Nombre', max_length=200)),
                ('perex', models.TextField(default='Perex')),
                ('text', models.TextField(default='Texto')),
                ('population', models.IntegerField(default=0)),
                ('categories', models.ManyToManyField(related_name='ciudades', to='content.categoria')),
                ('province', models.ForeignKey(default='Castilla la Mancha', on_delete=django.db.models.deletion.CASCADE, to='content.provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ciudades/')),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='content.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.ciudad')),
            ],
        ),
    ]
