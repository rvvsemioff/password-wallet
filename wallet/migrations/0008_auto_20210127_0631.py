# Generated by Django 3.1.3 on 2021-01-27 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0007_logs_isblocked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logs',
            name='isBlocked',
        ),
        migrations.AddField(
            model_name='logs',
            name='blockadeTime',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
