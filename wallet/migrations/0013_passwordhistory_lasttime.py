# Generated by Django 3.1.3 on 2021-01-28 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0012_auto_20210128_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordhistory',
            name='lastTime',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
