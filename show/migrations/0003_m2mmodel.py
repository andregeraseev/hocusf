# Generated by Django 4.1 on 2022-09-07 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0002_nomelista_show_banner_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='M2MModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='show.show')),
                ('field2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='show.nomelista')),
            ],
            options={
                'unique_together': {('field1', 'field2')},
            },
        ),
    ]
