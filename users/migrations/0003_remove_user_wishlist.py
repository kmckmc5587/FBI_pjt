# Generated by Django 3.2.13 on 2022-11-03 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='wishlist',
        ),
    ]
