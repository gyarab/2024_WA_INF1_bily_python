# Generated by Django 5.1.4 on 2025-03-25 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resena',
            name='rating',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='resena',
            name='text',
            field=models.TextField(default='Texto'),
        ),
    ]
