import os

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from pytils.translit import slugify
from django.urls import reverse

from PayTracker.settings import BASE_DIR


class Profile(models.Model):
    """Профиль автоматически создается, после регистрации Юзера"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Avatar', upload_to='avatars', blank=True,
                               default=os.path.join(BASE_DIR, 'media/avatars/nophoto.jpg'))
    first_name = models.CharField('First Name', max_length=50, blank=True)
    last_name = models.CharField('Last Name', max_length=50, blank=True)
    slug = models.SlugField('Url', unique=True, max_length=60)
    bio = models.TextField('Bio', max_length=200, default='add bio')
    created_date = models.DateTimeField('Created date', auto_now_add=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        """Автоматическое создание слага для профиля"""
        self.slug = str(slugify(self.user))
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'profile_slug': self.slug})

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """Если Юзер создан, то создается Профиль и завязывается на Юзере"""

        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """Сохранение Профиля"""

        instance.profile.save()


