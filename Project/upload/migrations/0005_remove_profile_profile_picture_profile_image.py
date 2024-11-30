# Generated by Django 4.2.2 on 2024-05-16 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
