# Generated by Django 5.2.3 on 2025-06-25 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=14)),
                ('data_nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=200)),
                ('cep', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=200)),
                ('qtd_equipamentos', models.IntegerField(blank=True, default=0, null=True)),
                ('detalhe_equipamento', models.CharField(max_length=200)),
                ('qtd_chamados', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.CharField(max_length=200)),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bairro_cliente', to='clientes.bairro')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cidade_cliente', to='clientes.cidade')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='estado_cliente', to='clientes.estado')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nivel_cliente', to='clientes.estado')),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]
