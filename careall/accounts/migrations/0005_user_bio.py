# Generated by Django 2.2.12 on 2020-05-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]