# Generated by Django 2.2 on 2021-09-07 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20210906_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='linedata',
            name='bandwidth_size',
            field=models.CharField(default=1, max_length=200, verbose_name='带宽大小'),
            preserve_default=False,
        ),
    ]
