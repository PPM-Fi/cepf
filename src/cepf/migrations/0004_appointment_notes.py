# Generated by Django 3.0.3 on 2020-02-25 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cepf', '0003_auto_20200223_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]