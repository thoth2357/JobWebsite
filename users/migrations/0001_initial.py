# Generated by Django 4.0.5 on 2022-07-06 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueId', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_images')),
                ('ethnicity', models.CharField(choices=[('Black', 'Black'), ('White', 'White'), ('Coloured', 'Coloured'), ('Indian', 'Indian'), ('Chinese', 'Chinese')], default='Black', max_length=200)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('date_birth', models.DateField()),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=200)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Widowed', 'Widowed'), ('Divorced', 'Divorced')], default='Single', max_length=200)),
                ('addressLine1', models.CharField(max_length=200, null=True)),
                ('addressLine2', models.CharField(max_length=200, null=True)),
                ('suburb', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('province', models.CharField(choices=[('Gauteng', 'Gauteng'), ('Mpumalanga', 'Mpumalanga'), ('Free-state', 'Free-state'), ('North-west', 'North-west'), ('Limpopo', 'Limpopo'), ('Western-cape', 'Western-cape'), ('Nothern-cape', 'Nothern-cape'), ('Eastern-cape', 'Eastern-cape'), ('Kwazulu-natal', 'Kwazulu-natal')], default='Gauteng', max_length=200)),
                ('phoneNumber', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_updated', models.DateTimeField()),
                ('cover_letter', models.FileField(upload_to='resumes')),
                ('cv', models.FileField(upload_to='resumes')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
