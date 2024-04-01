# Generated by Django 5.0.3 on 2024-04-01 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Central', '0002_cliente_cadastro_em_alter_despesa_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cadastro_em',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 22, 7, 33, 200247)),
        ),
        migrations.AlterField(
            model_name='despesa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 22, 7, 33, 200247)),
        ),
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 31, 22, 7, 33, 200247)),
        ),
    ]