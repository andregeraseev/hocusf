# Generated by Django 4.1 on 2022-09-08 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0019_alter_nomelista_nome_m2mmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='M2MModel',
        ),
    ]