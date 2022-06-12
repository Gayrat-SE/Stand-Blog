# Generated by Django 4.0.2 on 2022-03-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0009_remove_photo_post_post_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
        migrations.AddField(
            model_name='photo',
            name='post',
            field=models.ManyToManyField(related_name='posts', to='myproject.Post'),
        ),
    ]
