# Generated by Django 2.2.9 on 2020-01-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersettings', '0017_auto_20200115_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialurl',
            name='type',
            field=models.CharField(choices=[('twitter', 'Twitter'), ('medium', 'Medium'), ('linkedin', 'LinkedIn'), ('facebook', 'Facebook'), ('github', 'Github'), ('pintrest', 'Pintrest')], default='other', max_length=25, verbose_name='URL Type'),
        ),
    ]