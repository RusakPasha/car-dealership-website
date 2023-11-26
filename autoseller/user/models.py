from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Аватар", default="static/avatars/profile.png", upload_to='static/avatars')
    name = models.CharField(max_length=30, default="Имя")
    second_name = models.CharField(max_length=30, default="Фамилия")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return '/user/profile'

    class Meta:
        verbose_name = 'Информация о пользователе'
        verbose_name_plural = 'Информация о пользователях'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.customuser.save()
    except CustomUser.DoesNotExist:
        CustomUser.objects.create(user=instance)
