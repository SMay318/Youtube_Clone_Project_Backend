# Generated by Django 3.2.9 on 2021-11-09 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0004_comment_videoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='reply',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='youtube.comment'),
            preserve_default=False,
        ),
    ]