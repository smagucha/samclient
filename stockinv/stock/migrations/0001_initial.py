# Generated by Django 3.1.6 on 2021-02-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Brand', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('origin', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('dimension', models.CharField(max_length=100)),
                ('measurement', models.CharField(max_length=100)),
                ('storingmethod', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('cost', models.PositiveIntegerField()),
                ('retailprice', models.PositiveIntegerField()),
                ('size', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=100)),
                ('LotNo', models.PositiveIntegerField()),
                ('product_type', models.CharField(max_length=100)),
            ],
        ),
    ]