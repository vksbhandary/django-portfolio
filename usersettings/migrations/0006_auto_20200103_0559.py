# Generated by Django 2.2.7 on 2020-01-03 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersettings', '0005_auto_20200103_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialurl',
            name='type',
            field=models.CharField(choices=[('pintrest', 'Pintrest'), ('linkedin', 'LinkedIn'), ('github', 'Github'), ('medium', 'Medium'), ('facebook', 'Facebook'), ('twitter', 'Twitter')], default='other', max_length=25, verbose_name='URL Type'),
        ),
    ]