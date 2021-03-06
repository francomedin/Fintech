# Generated by Django 3.2.5 on 2022-02-08 19:19

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital', models.FloatField()),
                ('fecha_prestamo', models.DateField()),
                ('tasa_interes', models.FloatField()),
                ('cant_cuota', models.IntegerField()),
                ('monto_cuota', models.FloatField(default=0)),
                ('activo', models.BooleanField(default=True)),
                ('situacion', models.CharField(choices=[('Pagando', 'Al dia'), ('Mora Temprana', 'Atraso entre 1 y 30 días'), ('Mora Tardia', 'Atraso > 30 días'), ('Situacion Judicial', 'Atraso > 90 días')], default='Pagando', max_length=20)),
                ('titular', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='cliente.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacion', models.CharField(choices=[('Pagado', 'Pagado'), ('Pendiente', 'Pendiente de Pago'), ('Pago parcial', 'Pago Parcial'), ('No realizo Pago', 'No realizo Pago')], default='Pendiente', max_length=30)),
                ('capital_amortizable', models.FloatField()),
                ('amortizacion', models.FloatField(default=0)),
                ('interes', models.FloatField()),
                ('numero_cuota', models.PositiveIntegerField()),
                ('monto_cuota', models.FloatField()),
                ('total_pagado', models.FloatField(default=0)),
                ('fecha_pago', models.DateField()),
                ('credito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credito_pago', to='credito.credito')),
            ],
        ),
        migrations.CreateModel(
            name='Mora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_mora', models.CharField(blank=True, max_length=50, null=True)),
                ('monto_mora', models.FloatField(default=0)),
               
                ('cuota', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='credito.cuota')),
            ],
        ),
    ]
