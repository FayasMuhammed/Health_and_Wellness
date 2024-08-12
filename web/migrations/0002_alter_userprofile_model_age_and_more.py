# Generated by Django 5.0.3 on 2024-08-07 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile_model',
            name='age',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile_model',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile_model',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile_model',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile_model',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='userprofile_model',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
