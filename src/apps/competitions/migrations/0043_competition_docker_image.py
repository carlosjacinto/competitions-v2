# Generated by Django 2.1.2 on 2019-08-09 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0042_auto_20190808_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='docker_image',
            field=models.CharField(default='codalab/codalab-legacy:py3', max_length=128),
        ),
    ]