# Generated by Django 4.1 on 2022-09-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0016_alter_nomelista_nome_alter_show_titulo_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomelista',
            name='nome',
            field=models.CharField(max_length=100, unique='horario_do_show'),
        ),
    ]