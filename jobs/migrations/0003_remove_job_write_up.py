# Generated by Django 2.1.2 on 2018-11-18 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_write_up'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='write_up',
        ),
    ]
