# Generated by Django 2.2.9 on 2020-01-17 06:16

from django.db import migrations
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20200115_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featuredthumburl',
        ),
        migrations.RemoveField(
            model_name='post',
            name='featuredurl',
        ),
        migrations.AlterField(
            model_name='post',
            name='featuredimage',
            field=posts.models.CloudinaryFieldFix(blank=True, default=None, max_length=255, null=True, verbose_name='Featured image'),
        ),
        migrations.AlterField(
            model_name='postsettings',
            name='default_featured',
            field=posts.models.CloudinaryFieldFix(blank=True, default=None, max_length=255, null=True, verbose_name='Default featured image'),
        ),
        migrations.AlterField(
            model_name='postsettings',
            name='default_thumb',
            field=posts.models.CloudinaryFieldFix(blank=True, default=None, max_length=255, null=True, verbose_name='Default featured thumbnail'),
        ),
    ]