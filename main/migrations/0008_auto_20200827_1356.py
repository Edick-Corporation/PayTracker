# Generated by Django 3.1 on 2020-08-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200827_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['date'], 'verbose_name': 'Purchase', 'verbose_name_plural': 'Purchases'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ['name'], 'verbose_name': 'Type', 'verbose_name_plural': 'Types'},
        ),
        migrations.AlterField(
            model_name='purchase',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Cost'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Type of Purchase'),
        ),
    ]