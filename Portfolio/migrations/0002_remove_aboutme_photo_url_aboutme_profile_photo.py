# Generated by Django 5.0 on 2023-12-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='photo_url',
        ),
        migrations.AddField(
            model_name='aboutme',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/'),
        ),
    ]