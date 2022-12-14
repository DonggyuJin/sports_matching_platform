# Generated by Django 4.0.3 on 2022-08-26 03:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_check', models.CharField(max_length=20)),
                ('match_check', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MatchSports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sports_name', models.CharField(max_length=50)),
                ('sports_date', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('max_apply', models.PositiveIntegerField(default=1, verbose_name='max_apply')),
                ('apply_count', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(1)])),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('hits', models.PositiveIntegerField(default=1, verbose_name='hits')),
                ('apply_state', models.ManyToManyField(related_name='apply_count', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_match', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
