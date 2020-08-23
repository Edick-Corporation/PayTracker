from django.db import models
from django.urls import reverse

from main.models import Purchase


class Statistics(models.Model):
    purchases = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    slug = models.SlugField('Url', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистки'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('statistics_detail', kwargs={'statistics_pk': self.pk})