# Generated by Django 3.0.2 on 2020-02-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
            ],
        ),
    ]
