# Generated by Django 3.1 on 2020-08-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200827_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Стоимость'),
        ),
    ]