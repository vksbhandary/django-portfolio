# Generated by Django 2.2.9 on 2020-01-15 11:25

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersettings', '0016_auto_20200115_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='thumburl',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='iconurl',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='imageurl',
        ),
        migrations.AlterField(
            model_name='projects',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True, verbose_name='Thumbnail'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='icon',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True, verbose_name='Favicon'),
        ),
        migrations.AlterField(
            model_name='socialurl',
            name='type',
            field=models.CharField(choices=[('github', 'Github'), ('facebook', 'Facebook'), ('medium', 'Medium'), ('twitter', 'Twitter'), ('linkedin', 'LinkedIn'), ('pintrest', 'Pintrest')], default='other', max_length=25, verbose_name='URL Type'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, default=None, max_length=255, null=True, verbose_name='Profile picture'),
        ),
    ]