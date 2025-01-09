# Generated by Django 5.1.1 on 2024-09-06 16:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoPublicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estado', models.CharField(choices=[('borrador', 'Borrador'), ('en_papelera', 'En Papelera'), ('publicado', 'Publicado')], default='borrador', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rol', models.CharField(max_length=50)),
                ('puede_publicar', models.BooleanField(default=False)),
                ('puede_editar', models.BooleanField(default=False)),
                ('puede_eliminar', models.BooleanField(default=False)),
                ('puede_asignar_roles', models.BooleanField(default=False)),
                ('puede_dejar_comentarios', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_noticia', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateField()),
                ('seccion', models.CharField(choices=[('Portada', 'Portada'), ('Política', 'Política'), ('Economía', 'Economía'), ('Cultura', 'Cultura'), ('Mundo', 'Mundo'), ('Deportes', 'Deportes')], default='Portada', max_length=100)),
                ('tags', models.CharField(max_length=200)),
                ('imagen_cabecera', models.ImageField(upload_to='noticias/')),
                ('solo_para_subscriptores', models.BooleanField(default=False)),
                ('contenido', models.TextField(default='default content')),
                ('tiene_comentarios', models.BooleanField(default=False)),
                ('estado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diarioback.estadopublicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_imagen', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes_noticias/')),
                ('url', models.URLField(blank=True, null=True)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='diarioback.noticia')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('respuesta', models.TextField(blank=True, null=True)),
                ('fecha_respuesta', models.DateTimeField(blank=True, null=True)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='diarioback.noticia')),
            ],
        ),
        migrations.CreateModel(
            name='Publicidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_anuncio', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('url_destino', models.URLField()),
                ('impresiones', models.IntegerField()),
                ('clics', models.IntegerField()),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publicidades', to='diarioback.noticia')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=128)),
                ('foto_perfil', models.ImageField(upload_to='perfiles/')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trabajadores', to='diarioback.rol')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noticias', to='diarioback.trabajador'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=128)),
                ('foto_perfil', models.ImageField(upload_to='perfiles/')),
                ('esta_subscrito', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
