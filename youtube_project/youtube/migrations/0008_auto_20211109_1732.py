# Generated by Django 3.2.9 on 2021-11-09 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0007_rename_comment_id_reply_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
    ]