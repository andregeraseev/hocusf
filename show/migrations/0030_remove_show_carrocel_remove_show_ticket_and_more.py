# Generated by Django 4.1 on 2022-09-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0029_alter_show_descricao_show'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='carrocel',
        ),
        migrations.RemoveField(
            model_name='show',
            name='ticket',
        ),
        migrations.AddField(
            model_name='show',
            name='chave_pix',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]