# Generated by Django 5.1.1 on 2024-10-06 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diarioback', '0025_userprofile_descripcion_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='descripcion_usuario',
            field=models.TextField(blank=True, null=True),
        ),
    ]
