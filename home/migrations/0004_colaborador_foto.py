# Generated by Django 5.1.5 on 2025-01-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_celular'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='colaboradores_fotos/'),
        ),
    ]