# Generated by Django 4.1.1 on 2022-11-24 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_rename_title_song_name_alter_album_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.TextField(null=True),
        ),
    ]