from django.db import models
from django.urls import reverse


class Purchase(models.Model):
    type = models.CharField('Тип покупки', max_length=100)
    cost = models.PositiveIntegerField('Стоимость')
    slug = models.SlugField('Url', max_length=110, unique=True)
    degree_of_importance = models.SmallIntegerField('Степень важности', default=0)
    date = models.DateTimeField('Когда была сделана покупка', auto_now_add=True)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        ordering = ['date']

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('purchase_detail', kwargs={'purchase_pk': self.pk})
