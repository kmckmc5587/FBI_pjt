# Generated by Django 3.2.13 on 2022-11-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]