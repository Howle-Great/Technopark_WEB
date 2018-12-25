# Generated by Django 2.1.2 on 2018-12-23 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0006_auto_20181105_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Одобрен автором вопроса'),
        ),
        migrations.AddField(
            model_name='like',
            name='answer',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='question.Answer'),
            preserve_default=False,
        ),
    ]
