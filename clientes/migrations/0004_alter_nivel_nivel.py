# Generated by Django 5.2.3 on 2025-06-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_statusclientes_alter_clientes_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nivel',
            name='nivel',
            field=models.IntegerField(),
        ),
    ]
