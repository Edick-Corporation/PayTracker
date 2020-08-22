from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Type(MPTTModel):
    name = models.CharField('Тип покупки', max_length=100)
    slug = models.SlugField('Url', max_length=110)
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='children'
    )

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('type_detail', kwargs={'type_slug': self.slug})


class Purchase(models.Model):
    type = models.ForeignKey(Type, related_name='Type', on_delete=models.CASCADE)
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
        return reverse('purchase_detail', kwargs={'type_slug': self.type.slug, 'purchase_pk': self.pk})
