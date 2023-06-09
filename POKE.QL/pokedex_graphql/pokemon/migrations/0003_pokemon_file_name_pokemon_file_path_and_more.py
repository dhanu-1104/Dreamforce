# Generated by Django 4.1.7 on 2023-03-31 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_pokemon_name_pokemon_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='file_name',
            field=models.CharField(default='normal', max_length=255),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='file_path',
            field=models.CharField(default='normal', max_length=255),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='strength',
            field=models.CharField(max_length=250),
        ),
    ]
