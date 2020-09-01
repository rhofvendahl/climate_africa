from django.db import models
from django.contrib.auth.models import User # unsure how to do this with string, my preference
# from cities_light.abstract_models import AbstractCity, AbstractRegion, AbstractCountry
# from cities_light.receivers import connect_default_signals (not necessary at this time)


class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=160, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('common.Tag', related_name='users')
    city = models.ForeignKey('cities_light.City', null=True, blank=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'ID: {self.id}, title: {self.title}'

class Tag(models.Model):
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    is_starter = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'ID: {self.id}, name: {self.name}, is_starter: {str(self.is_starter)}'

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    default_city = models.ForeignKey('cities_light.City', null=True, blank=True, on_delete=models.PROTECT)
    is_organization = models.BooleanField(default=False)

    def __str__(self):
        return f'ID: {self.id}, username: {self.user.username}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
