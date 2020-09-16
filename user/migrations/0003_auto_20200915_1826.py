# Generated by Django 3.1 on 2020-09-15 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200827_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='Avatar'),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='add bio', max_length=200, verbose_name='Bio'),
        ),
    ]
