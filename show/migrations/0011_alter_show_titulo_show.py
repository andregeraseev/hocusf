# Generated by Django 4.1 on 2022-09-08 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0010_alter_nomelista_nome_alter_show_titulo_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='titulo_show',
            field=models.CharField(error_messages={'unique': 'Este CPF ja foi cadastrado no show.'}, max_length=100, unique='lista_reserva_sr'),
        ),
    ]