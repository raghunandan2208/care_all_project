# Generated by Django 2.2.12 on 2020-05-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200526_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_elder_profile',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_younger_profile',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
