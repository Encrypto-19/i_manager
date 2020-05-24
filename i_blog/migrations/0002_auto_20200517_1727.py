# Generated by Django 3.0.6 on 2020-05-17 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('i_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='perks',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='tagline',
            field=models.TextField(default='Tagline here'),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('para', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='i_blog.Company')),
            ],
        ),
    ]