# Generated by Django 4.1 on 2022-09-15 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0024_show_carrocel_show_pix'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='quadrado',
            field=models.ImageField(blank=True, upload_to='static/banners'),
        ),
    ]