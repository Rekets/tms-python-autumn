# Generated by Django 3.1.6 on 2021-03-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0027_auto_20210308_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='all_duration',
            field=models.CharField(blank=True, max_length=30, verbose_name='all duration'),
        ),
    ]
