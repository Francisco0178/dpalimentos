# Generated by Django 3.2.4 on 2021-06-17 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('embarques', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embarque',
            name='ctr',
            field=models.IntegerField(),
        ),
    ]
