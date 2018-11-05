# Generated by Django 2.1.2 on 2018-11-05 18:30

from django.db import migrations, models
import django.utils.timezone
import question.managers


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20181104_1442'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', question.managers.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='rating',
            field=models.IntegerField(default=0, verbose_name="User's Rating"),
        ),
        migrations.AddField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name="User's Registration Date"),
        ),
    ]
