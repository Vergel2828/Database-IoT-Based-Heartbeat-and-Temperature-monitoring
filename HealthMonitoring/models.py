from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.timezone import now
import datetime

optional = {
    'null': True,
    'blank': True
}


class Profile(models.Model):
    
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female')
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=255)
    birthday = models.DateField(default=datetime.date.today)
    age = models.IntegerField(**optional)
    gender = models.CharField(
            max_length = 2,
            choices = gender_choices,
            default = 'M',
        )
    cellphone_number = models.CharField(max_length=11, **optional)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "Users Profile"

"""  
---Auto Create Profile when user is created---

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
"""

class HeartRateData(models.Model):
    
    status_choices = (
        ('EB', 'Excellent'),
        ('GB', 'Good'),
        ('AA', 'Above Average'),
        ('AB', 'Average'),
        ('BA', 'Below Average'),
        ('PB', 'Poor'),
        )

    data_from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    heart_rate_reading = models.IntegerField()
    time_recorded = models.DateTimeField(default=now)
    status = models.CharField(
            max_length = 6,
            choices = status_choices,
            default = 'GB',
        )


    def __str__(self):
        return "%d" %(self.heart_rate_reading)


class TemperatureData(models.Model):

    status_choices = (
        ('HP', 'Hypothermia'),
        ('NT', 'Normal'),
        ('FE', 'Fever'),
        ('HX', 'Hyperpyrexia'),
        )

    data_from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    temperature_reading = models.DecimalField(max_digits=4, decimal_places=2)
    time_recorded = models.DateTimeField(default=now)
    status = models.CharField(
            max_length = 4,
            choices = status_choices,
            default = 'NT',
        )


    def __str__(self):
        return "%f" %(self.temperature_reading)
