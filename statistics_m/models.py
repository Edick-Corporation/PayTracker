from django.db import models
from django.urls import reverse

from main.models import Purchase


class Statistics(models.Model):
    purchases = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    slug = models.SlugField('Url', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Statistics'
        verbose_name_plural = 'Statistics'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('statistics_detail', kwargs={'statistics_pk': self.pk})


# class PostWithStatistics(models.Model):
#     statistics = models.ForeignKey(Statistics, related_name='Statistics', on_delete=models.CASCADE)
#     title = models.CharField('Заголовок', max_length=200)
#     text = models.TextField('Текст', max_length=1000)
