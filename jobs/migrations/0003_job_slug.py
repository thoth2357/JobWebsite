# Generated by Django 4.0.7 on 2022-09-19 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_remove_job_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]