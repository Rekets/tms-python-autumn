from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=30, blank=True)
    height = models.CharField(max_length=30, blank=True)
    weight = models.CharField(max_length=3, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, default='/media/media/Koala_30BhBrc.jpg')
    all_length = models.CharField('all length', max_length=30, blank=True, )


    def __str__(self):
        return self.user.username


class Register(models.Model):
    """
    Класс регистрации профиля
    """
    pass


class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name_activity = models.CharField('name_activity', max_length=30,
                                     blank=True)
    rout_length = models.CharField('rout_length', max_length=30, blank=True)
    duration = models.CharField('duration', max_length=30, blank=True)
    date = models.DateTimeField('date/Time')

    weight = models.CharField(max_length=3, blank=True)
    calories = models.CharField('calories', max_length=5, blank=True)

    all_length = models.CharField('all length', max_length=30, blank=True,)


    def __str__(self):
        return self.name_activity
