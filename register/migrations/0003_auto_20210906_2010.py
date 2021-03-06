# Generated by Django 2.2 on 2021-09-06 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20210901_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='softdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=200, verbose_name='软件名称')),
                ('delay_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='到期时间')),
                ('supplier_name', models.CharField(max_length=200, verbose_name='供应商名称')),
                ('master_people', models.CharField(max_length=200, verbose_name='负责人')),
                ('email_address', models.CharField(max_length=200, verbose_name='邮箱地址')),
            ],
            options={
                'verbose_name': '软件记录',
                'verbose_name_plural': '软件记录',
            },
        ),
        migrations.AlterModelOptions(
            name='linedata',
            options={'verbose_name': '网络专线记录', 'verbose_name_plural': '网络专线记录'},
        ),
        migrations.AddField(
            model_name='linedata',
            name='cost',
            field=models.CharField(default=1, max_length=200, verbose_name='价格'),
            preserve_default=False,
        ),
    ]
