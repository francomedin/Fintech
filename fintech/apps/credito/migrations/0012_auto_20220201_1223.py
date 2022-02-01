# Generated by Django 3.2.5 on 2022-02-01 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credito', '0011_alter_cuota_situacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='situacion',
            field=models.CharField(choices=[('Pagando', 'Al dia'), ('Mora Temprana', 'Atraso entre 1 y 30 días'), ('Mora Tardia', 'Atraso > 30 días'), ('Situacion Judicial', 'Atraso > 90 días')], default='Pagando', max_length=20),
        ),
        migrations.AlterField(
            model_name='cuota',
            name='credito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='credito_pago', to='credito.credito'),
        ),
    ]