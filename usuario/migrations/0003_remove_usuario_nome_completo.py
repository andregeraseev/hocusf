# Generated by Django 4.1 on 2022-09-12 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_nome_completo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nome_completo',
        ),
    ]
