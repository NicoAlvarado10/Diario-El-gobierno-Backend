# Generated by Django 5.1.1 on 2025-01-31 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diarioback', '0036_rename_tags_noticia_palabras_clave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='seccion1',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='seccion2',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='seccion3',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='seccion4',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='seccion5',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='seccion6',
        ),
    ]
