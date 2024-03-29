# Generated by Django 5.0.3 on 2024-03-05 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planeacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_actividad', models.CharField(choices=[('estimacion', 'Estimación'), ('diseno_cp', 'Diseño CP'), ('ejecucion', 'Ejecución')], max_length=20)),
                ('fecha', models.DateField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planeaciones', to='proyectos.proyecto')),
            ],
            options={
                'unique_together': {('proyecto', 'tipo_actividad')},
            },
        ),
    ]
