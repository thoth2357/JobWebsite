# Generated by Django 4.0.7 on 2022-11-18 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_job_full_job_qualifactions_dutes_all'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='full_job_qualifactions_dutes_all',
            new_name='full_job_qualifications_duties_all',
        ),
    ]
