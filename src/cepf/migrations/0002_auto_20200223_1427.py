# Generated by Django 3.0.3 on 2020-02-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cepf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='feedback',
        ),
        migrations.AddField(
            model_name='appointment',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
