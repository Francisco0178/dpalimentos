# Generated by Django 4.0 on 2021-12-10 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]