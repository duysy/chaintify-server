# Generated by Django 4.1.1 on 2022-11-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_song_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='cover',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
