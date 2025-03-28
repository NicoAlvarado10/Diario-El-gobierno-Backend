# Generated by Django 5.1.1 on 2025-03-28 22:51

import diarioback.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diarioback', '0046_alter_noticia_categorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='categorias',
            field=models.TextField(blank=True, null=True, validators=[diarioback.models.Noticia.validate_categorias]),
        ),
    ]
