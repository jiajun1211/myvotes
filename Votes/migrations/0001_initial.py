# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('u_name', models.CharField(max_length=100)),
                ('u_img', models.URLField()),
                ('v_name', models.CharField(max_length=200)),
                ('v_title', models.CharField(max_length=200)),
                ('v_leftItemText', models.CharField(max_length=200)),
                ('v_rightItemText', models.CharField(max_length=200)),
                ('v_leftItemImg', models.URLField()),
                ('v_rightItemImg', models.URLField()),
                ('v_leftCount', models.IntegerField()),
                ('v_rightCount', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
