# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20150115_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='time',
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 1, 17, 18, 59, 48, 878000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
