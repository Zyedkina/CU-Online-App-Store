# Generated by Django 2.1.5 on 2019-02-11 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20190211_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appprofile',
            old_name='topic',
            new_name='signup',
        ),
        migrations.AlterField(
            model_name='appprofile',
            name='appname',
            field=models.CharField(max_length=264, unique=True),
        ),
    ]
