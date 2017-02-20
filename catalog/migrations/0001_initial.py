# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('category', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='catalog.Unit'),
        ),
    ]
