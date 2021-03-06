# Generated by Django 2.1.2 on 2018-11-04 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20181104_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='author',
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={},
        ),
        migrations.AddField(
            model_name='answer',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Время ответа'),
        ),
        migrations.AddField(
            model_name='answer',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг ответа'),
        ),
        migrations.AddField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг вопроса'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
