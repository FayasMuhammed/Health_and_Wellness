# Generated by Django 5.0.3 on 2024-08-07 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_userprofile_model_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile_model',
            name='profile_picture',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
    ]
