# Generated by Django 2.1.2 on 2018-11-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_job_write_up'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='art',
            field=models.CharField(default="Art: 'TITLE' - ARTIST (YEAR)", max_length=200),
        ),
        migrations.AddField(
            model_name='job',
            name='song',
            field=models.CharField(default="Song: 'TITLE' - ARTIST (YEAR)", max_length=200),
        ),
    ]