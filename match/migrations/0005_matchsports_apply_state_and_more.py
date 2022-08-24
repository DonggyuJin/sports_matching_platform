# Generated by Django 4.0.3 on 2022-08-23 14:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('match', '0004_remove_matchsports_apply_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchsports',
            name='apply_state',
            field=models.ManyToManyField(related_name='apply_count', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='matchsports',
            name='apply_count',
        ),
        migrations.AddField(
            model_name='matchsports',
            name='apply_count',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)]),
        ),
    ]