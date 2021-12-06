# Generated by Django 3.2.8 on 2021-11-17 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(verbose_name='imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('area', models.IntegerField(verbose_name='Area en mts')),
                ('banio', models.CharField(choices=[('P', 'Privado'), ('C', 'Compartido')], max_length=1, verbose_name='Baño ')),
                ('ciudad', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('ubicacion', models.CharField(max_length=50, verbose_name='Ubicacion aproximada')),
                ('descripcion', models.TextField(verbose_name='Breve Descripcion')),
                ('estrato', models.IntegerField(verbose_name='Estrato socioeconomico')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('estacionamiento', models.BooleanField(verbose_name='Estacionamiento')),
                ('created_data', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('modified_data', models.DateField(auto_now_add=True, verbose_name='Fecha de Modificacion')),
                ('deleted_data', models.DateField(auto_now_add=True, verbose_name='Fecha de Eliminacion')),
            ],
            options={
                'verbose_name': 'Modelo Room',
                'verbose_name_plural': 'Modelos Room',
            },
        ),
    ]
