# Generated by Django 3.1.6 on 2021-03-08 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0029_activity_av_speed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='av_speed',
            field=models.CharField(blank=True, max_length=30, verbose_name='av speed'),
        ),
    ]
