# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-30 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=6)),
                ('is_residential', models.BooleanField()),
                ('is_inactive', models.BooleanField()),
                ('version', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255, unique=True)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='keyissue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255, unique=True)),
                ('start_date', models.DateTimeField(null=True)),
                ('End_date', models.DateTimeField(null=True)),
                ('ownder_id', models.CharField(max_length=6, null=True)),
                ('person_id', models.CharField(max_length=6, null=True)),
                ('note', models.CharField(blank=True, max_length=255, null=True)),
                ('key_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keys.key')),
            ],
        ),
        migrations.CreateModel(
            name='keystatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255, unique=True)),
                ('label', models.CharField(max_length=100)),
                ('order', models.IntegerField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='keytype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=6)),
                ('manu_info', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True)),
                ('building_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='keys.building')),
            ],
        ),
        migrations.AddField(
            model_name='keyissue',
            name='keystatus_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keys.keystatus'),
        ),
        migrations.AddField(
            model_name='key',
            name='keytype_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keytype_id', to='keys.keytype'),
        ),
    ]
