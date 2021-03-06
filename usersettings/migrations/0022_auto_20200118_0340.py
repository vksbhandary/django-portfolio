# Generated by Django 2.2.9 on 2020-01-18 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersettings', '0021_auto_20200117_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialurl',
            name='type',
            field=models.CharField(choices=[('linkedin', 'LinkedIn'), ('github', 'Github'), ('medium', 'Medium'), ('twitter', 'Twitter'), ('pintrest', 'Pintrest'), ('facebook', 'Facebook')], default='other', max_length=25, verbose_name='URL Type'),
        ),
    ]
