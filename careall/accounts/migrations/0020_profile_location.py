# Generated by Django 2.2.12 on 2020-07-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_completed_scheduled_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
