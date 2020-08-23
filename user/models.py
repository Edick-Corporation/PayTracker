from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from pytils.translit import slugify
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    slug = models.SlugField('Url', unique=True, max_length=60)
    created_date = models.DateTimeField('Дата создания профиля', auto_now_add=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = str(slugify(self.user)) + str(self.pk)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'profile_slug': self.slug})

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


