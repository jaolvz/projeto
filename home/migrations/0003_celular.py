# Generated by Django 5.1.5 on 2025-01-21 12:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_colaborador_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('responsavel', models.OneToOneField(default='Sem uso', on_delete=django.db.models.deletion.SET_DEFAULT, to='home.colaborador')),
            ],
        ),
    ]
