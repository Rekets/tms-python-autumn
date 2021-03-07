# Generated by Django 3.1.6 on 2021-03-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0021_profile_all_duration_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='all_duration',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='all_duration_profile',
        ),
        migrations.AddField(
            model_name='activity',
            name='all_length',
            field=models.CharField(blank=True, max_length=30, verbose_name='rout_length'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/media/media/Koala_30BhBrc.jpg', null=True, upload_to='images'),
        ),
    ]
