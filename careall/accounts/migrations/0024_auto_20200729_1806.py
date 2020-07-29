# Generated by Django 2.2.12 on 2020-07-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20200729_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.TextField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(default=0, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=0, max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='First name', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Last name', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
    ]
