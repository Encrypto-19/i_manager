# Generated by Django 3.0.6 on 2020-05-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('i_blog', '0003_auto_20200517_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='resume',
            field=models.FileField(blank=True, upload_to='resume_company'),
        ),
    ]
