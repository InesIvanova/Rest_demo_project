# Generated by Django 2.2 on 2019-04-19 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20190419_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
