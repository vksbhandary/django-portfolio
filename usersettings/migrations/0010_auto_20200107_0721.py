# Generated by Django 2.2.7 on 2020-01-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersettings', '0009_auto_20200107_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialurl',
            name='type',
            field=models.CharField(choices=[('pintrest', 'Pintrest'), ('github', 'Github'), ('facebook', 'Facebook'), ('linkedin', 'LinkedIn'), ('twitter', 'Twitter'), ('medium', 'Medium')], default='other', max_length=25, verbose_name='URL Type'),
        ),
    ]
