# Generated by Django 5.0 on 2023-12-21 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]