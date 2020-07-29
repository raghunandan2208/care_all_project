# Generated by Django 2.2.12 on 2020-07-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20200727_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile/default-profile.jpg', upload_to='profile/'),
        ),
    ]
