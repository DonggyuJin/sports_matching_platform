# Generated by Django 4.0.3 on 2022-08-26 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='freecontent',
            name='hits',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
