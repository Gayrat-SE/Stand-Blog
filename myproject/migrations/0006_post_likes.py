# Generated by Django 4.0.2 on 2022-02-27 21:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myproject', '0005_remove_post_likes_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]