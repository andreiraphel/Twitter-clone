# Generated by Django 5.0.7 on 2024-07-15 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_email_user_joined_date_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='joined_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
