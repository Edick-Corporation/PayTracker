# Generated by Django 3.1 on 2020-08-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200827_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Cost $'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
    ]
