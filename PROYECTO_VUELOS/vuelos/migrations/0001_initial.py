# Generated by Django 3.1.3 on 2021-03-09 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuerto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=3)),
                ('ciudad', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arribos', to='vuelos.aeropuerto')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salidas', to='vuelos.aeropuerto')),
            ],
        ),
    ]
