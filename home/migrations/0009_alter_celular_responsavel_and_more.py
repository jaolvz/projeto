# Generated by Django 5.1.5 on 2025-01-22 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_colaborador_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celular',
            name='responsavel',
            field=models.OneToOneField(default='Estoque', on_delete=django.db.models.deletion.SET_DEFAULT, to='home.colaborador'),
        ),
        migrations.AlterField(
            model_name='computador',
            name='responsavel',
            field=models.OneToOneField(default='Estoque', on_delete=django.db.models.deletion.SET_DEFAULT, to='home.colaborador'),
        ),
    ]