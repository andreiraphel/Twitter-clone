# Generated by Django 5.0.6 on 2024-07-17 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='likes',
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweet_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
