# Generated by Django 3.1 on 2020-08-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200827_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='cost',
            field=models.IntegerField(verbose_name='Стоимость'),
        ),
    ]
