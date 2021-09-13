# Generated by Django 2.2 on 2021-09-01 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='linedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=200, verbose_name='专线名称')),
                ('delay_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='到期时间')),
            ],
        ),
    ]
