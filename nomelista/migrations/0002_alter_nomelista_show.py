# Generated by Django 4.1 on 2022-08-31 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0002_show'),
        ('nomelista', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomelista',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show.show'),
        ),
    ]
