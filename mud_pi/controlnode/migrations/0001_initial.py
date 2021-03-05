# Generated by Django 3.1.7 on 2021-03-05 21:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('zone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zone.zone')),
            ],
        ),
        migrations.CreateModel(
            name='ControlNodeUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbreviatedName', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ControlNodeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=50)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlnode.controlnodeunit')),
            ],
        ),
        migrations.CreateModel(
            name='ControlNodeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('value', models.FloatField()),
                ('datatype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlnode.controlnodetype')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlnode.controlnode')),
            ],
        ),
    ]
