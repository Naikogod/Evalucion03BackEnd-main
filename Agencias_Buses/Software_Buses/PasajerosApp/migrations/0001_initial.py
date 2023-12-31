# Generated by Django 2.2 on 2023-12-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=20, unique=True)),
                ('edad', models.IntegerField()),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('tipoPasajero', models.CharField(choices=[('Estudiante', 'Estudiante'), ('AdultoMayor', 'Adulto Mayor'), ('Frecuente', 'Frecuente'), ('Normal', 'Normal')], max_length=20)),
            ],
        ),
    ]
