# Generated by Django 3.1.2 on 2020-11-18 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_auto_20201104_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='password',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
