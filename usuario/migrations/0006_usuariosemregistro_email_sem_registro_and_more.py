# Generated by Django 4.1 on 2022-10-06 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_alter_usuariosemregistro_usuario_sem_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariosemregistro',
            name='email_sem_registro',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='usuariosemregistro',
            name='senha_unica',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
