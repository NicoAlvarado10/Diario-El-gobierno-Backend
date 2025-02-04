# Generated by Django 5.1.1 on 2025-01-31 14:52

import diarioback.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diarioback', '0037_remove_noticia_seccion1_remove_noticia_seccion2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='categorias',
            field=models.TextField(blank=True, null=True, validators=[diarioback.models.Noticia.validate_categorias]),
        ),
    ]
