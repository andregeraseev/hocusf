# Generated by Django 4.1 on 2022-09-14 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0023_nomelista_sem_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='carrocel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='show',
            name='pix',
            field=models.BooleanField(default=False),
        ),
    ]