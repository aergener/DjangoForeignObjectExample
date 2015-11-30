# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock_id', models.IntegerField()),
                ('dateval', models.DateField()),
                ('price', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock_id', models.IntegerField()),
                ('dateval', models.DateField()),
                ('stock_name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='price',
            name='stock',
            field=app.models.ForeignObject(related_name=b'price', unique=True, to_fields=(b'stock_id', b'dateval'), to='app.Stock', from_fields=(b'stock_id', b'dateval')),
            preserve_default=True,
        ),
    ]
