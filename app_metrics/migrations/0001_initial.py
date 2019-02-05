# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gauge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('slug', models.SlugField(unique=True, max_length=60, verbose_name='slug')),
                ('current_value', models.DecimalField(default=0, verbose_name='current value', max_digits=15, decimal_places=6)),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=datetime.datetime.now, verbose_name='updated')),
            ],
            options={
                'verbose_name': 'gauge',
                'verbose_name_plural': 'gauges',
            },
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('slug', models.SlugField(unique=True, max_length=60, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'metric',
                'verbose_name_plural': 'metrics',
            },
        ),
        migrations.CreateModel(
            name='MetricDay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.BigIntegerField(default=0, verbose_name='number')),
                ('created', models.DateField(default=datetime.date.today, verbose_name='created')),
                ('metric', models.ForeignKey(verbose_name='metric', to='app_metrics.Metric', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'day metric',
                'verbose_name_plural': 'day metrics',
            },
        ),
        migrations.CreateModel(
            name='MetricItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.IntegerField(default=1, verbose_name='number')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='created')),
                ('metric', models.ForeignKey(verbose_name='metric', to='app_metrics.Metric', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'metric item',
                'verbose_name_plural': 'metric items',
            },
        ),
        migrations.CreateModel(
            name='MetricMonth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.BigIntegerField(default=0, verbose_name='number')),
                ('created', models.DateField(default=datetime.date.today, verbose_name='created')),
                ('metric', models.ForeignKey(verbose_name=b'metric', to='app_metrics.Metric', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'month metric',
                'verbose_name_plural': 'month metrics',
            },
        ),
        migrations.CreateModel(
            name='MetricSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('no_email', models.BooleanField(default=False, verbose_name='no e-mail')),
                ('send_daily', models.BooleanField(default=True, verbose_name='send daily')),
                ('send_weekly', models.BooleanField(default=False, verbose_name='send weekly')),
                ('send_monthly', models.BooleanField(default=False, verbose_name='send monthly')),
                ('email_recipients', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='email recipients')),
                ('metrics', models.ManyToManyField(to='app_metrics.Metric', verbose_name='metrics')),
            ],
            options={
                'verbose_name': 'metric set',
                'verbose_name_plural': 'metric sets',
            },
        ),
        migrations.CreateModel(
            name='MetricWeek',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.BigIntegerField(default=0, verbose_name='number')),
                ('created', models.DateField(default=datetime.date.today, verbose_name='created')),
                ('metric', models.ForeignKey(verbose_name='metric', to='app_metrics.Metric', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'week metric',
                'verbose_name_plural': 'week metrics',
            },
        ),
        migrations.CreateModel(
            name='MetricYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.BigIntegerField(default=0, verbose_name='number')),
                ('created', models.DateField(default=datetime.date.today, verbose_name='created')),
                ('metric', models.ForeignKey(verbose_name='metric', to='app_metrics.Metric', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'year metric',
                'verbose_name_plural': 'year metrics',
            },
        ),
    ]
