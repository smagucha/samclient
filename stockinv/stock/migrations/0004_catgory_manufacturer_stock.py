# Generated by Django 3.1.6 on 2021-03-01 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '0003_auto_20210301_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catgory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Brand', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('measurement', models.CharField(max_length=100)),
                ('storingmethod', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('cost', models.PositiveIntegerField()),
                ('retailprice', models.PositiveIntegerField()),
                ('size', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=100)),
                ('LotNo', models.PositiveIntegerField()),
                ('product_type', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.catgory')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.manufacturer')),
            ],
        ),
    ]
