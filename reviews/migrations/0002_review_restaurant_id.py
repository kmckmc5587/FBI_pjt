# Generated by Django 3.2.13 on 2022-11-01 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='Restaurant_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Restaurant.restaurant'),
            preserve_default=False,
        ),
    ]