# Generated by Django 3.0.6 on 2020-05-17 20:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('i_blog', '0002_auto_20200517_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='date_applied',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(default='Applied', max_length=50),
        ),
    ]
