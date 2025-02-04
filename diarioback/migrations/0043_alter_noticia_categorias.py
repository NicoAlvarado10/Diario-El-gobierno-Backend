# Generated by Django 5.1.1 on 2025-02-01 17:15

import diarioback.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diarioback', '0042_alter_noticia_categorias_alter_noticia_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='categorias',
            field=models.TextField(blank=True, null=True, validators=[diarioback.models.Noticia.validate_categorias]),
        ),
    ]
