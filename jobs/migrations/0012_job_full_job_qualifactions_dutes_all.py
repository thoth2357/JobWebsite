# Generated by Django 4.0.7 on 2022-10-28 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='full_job_qualifactions_dutes_all',
            field=models.TextField(blank=True, null=True),
        ),
    ]
