# Generated by Django 5.1.1 on 2024-09-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diarioback', '0003_noticia_imagen_cabecera_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='imagen_cabecera_file',
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagen_cabecera',
            field=models.URLField(default='https://example.com/default-image.jpg'),
        ),
    ]
