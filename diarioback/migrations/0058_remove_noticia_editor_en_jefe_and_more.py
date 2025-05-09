# Generated by Django 5.1.1 on 2025-04-20 19:46

import diarioback.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diarioback', '0057_trabajador_foto_perfil_temp_alter_noticia_categorias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='editor_en_jefe',
        ),
        migrations.RemoveField(
            model_name='trabajador',
            name='foto_perfil_temp',
        ),
        migrations.AddField(
            model_name='noticia',
            name='editores_en_jefe',
            field=models.ManyToManyField(blank=True, related_name='noticias_supervisadas', to='diarioback.trabajador', verbose_name='Editores en jefe'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='categorias',
            field=models.TextField(blank=True, null=True, validators=[diarioback.models.Noticia.validate_categorias]),
        ),
    ]
