# Generated by Django 3.1.14 on 2022-01-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dark_theme',
            field=models.BooleanField(default=False),
        ),
    ]
