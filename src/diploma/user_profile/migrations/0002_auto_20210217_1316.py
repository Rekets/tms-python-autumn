# Generated by Django 3.1.6 on 2021-02-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
