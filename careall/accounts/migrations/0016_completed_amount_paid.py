# Generated by Django 2.2.12 on 2020-07-27 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_younger_earnings'),
    ]

    operations = [
        migrations.AddField(
            model_name='completed',
            name='amount_paid',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]