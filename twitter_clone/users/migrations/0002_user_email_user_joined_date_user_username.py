# Generated by Django 5.0.7 on 2024-07-15 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
