# Generated by Django 3.1.2 on 2020-11-04 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='description',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='password',
            name='login',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='password',
            name='web_address',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='salt',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
