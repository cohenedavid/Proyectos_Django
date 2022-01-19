# Generated by Django 3.1.3 on 2021-03-17 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vuelos', '0002_delete_vuelo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('duracion', models.IntegerField()),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arribos', to='vuelos.aeropuerto')),
                ('origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salidas', to='vuelos.aeropuerto')),
            ],
        ),
    ]
