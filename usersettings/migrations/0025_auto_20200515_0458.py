# Generated by Django 2.2.12 on 2020-05-15 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersettings', '0024_auto_20200118_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='blogurl',
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='blog_featured_active',
            field=models.BooleanField(default=False, verbose_name='Activate Blog featured images'),
        ),
        migrations.AlterField(
            model_name='socialurl',
            name='type',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('linkedin', 'LinkedIn'), ('github', 'Github'), ('medium', 'Medium'), ('pintrest', 'Pintrest')], default='other', max_length=25, verbose_name='URL Type'),
        ),
    ]
