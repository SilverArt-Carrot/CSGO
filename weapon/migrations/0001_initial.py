# Generated by Django 3.0.2 on 2020-01-31 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gun', models.CharField(max_length=50)),
                ('which_cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weapon.Category')),
            ],
        ),
    ]
