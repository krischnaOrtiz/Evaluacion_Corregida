# Generated by Django 4.1 on 2022-12-26 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('anio_creacion', models.IntegerField()),
                ('campeon', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('dorsal', models.IntegerField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mundial_api.equipo')),
            ],
        ),
    ]