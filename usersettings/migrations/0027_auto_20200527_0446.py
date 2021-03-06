# Generated by Django 2.2.12 on 2020-05-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersettings', '0026_auto_20200516_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='fbappid',
            field=models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='Facebook App ID'),
        ),
        migrations.AlterField(
            model_name='socialurl',
            name='type',
            field=models.CharField(choices=[('linkedin', 'LinkedIn'), ('facebook', 'Facebook'), ('pintrest', 'Pintrest'), ('twitter', 'Twitter'), ('medium', 'Medium'), ('github', 'Github')], default='other', max_length=25, verbose_name='URL Type'),
        ),
    ]
