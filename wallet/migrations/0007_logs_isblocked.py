# Generated by Django 3.1.3 on 2021-01-13 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_logs'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='isBlocked',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
