# Generated by Django 5.2.4 on 2025-07-16 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0005_compra_delete_ordencompra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contacto', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='compra',
            old_name='precio_unitario',
            new_name='total',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='producto',
        ),
        migrations.AddField(
            model_name='compra',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.proveedor'),
        ),
    ]
