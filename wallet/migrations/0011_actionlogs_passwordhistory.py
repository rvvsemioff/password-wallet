# Generated by Django 3.1.3 on 2021-01-28 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0010_sharedpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=256, null=True)),
                ('web_address', models.CharField(max_length=256, null=True)),
                ('description', models.CharField(max_length=256, null=True)),
                ('login', models.CharField(max_length=256, null=True)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.user')),
            ],
        ),
        migrations.CreateModel(
            name='ActionLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(max_length=256)),
                ('accessTime', models.DateTimeField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.user')),
            ],
        ),
    ]
