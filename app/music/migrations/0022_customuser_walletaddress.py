# Generated by Django 4.1.1 on 2022-12-01 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0021_remove_song_ispublic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='walletAddress',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
