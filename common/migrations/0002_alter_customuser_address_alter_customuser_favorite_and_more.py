# Generated by Django 4.0.3 on 2022-08-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='favorite',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='introduction',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
